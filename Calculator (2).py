import math
import tkinter as tk


class ScientificCalculator:

    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("420x640")
        self.root.configure(bg="#121212")

        # Ensure window is resizable and adapts gracefully
        self.root.minsize(360, 540)

        # Display screen for inputs and results
        self.display = tk.Entry(
            root,
            font=("Arial", 28, "bold"),
            bg="#121212",
            fg="white",
            borderwidth=0,
            justify="right",
        )
        self.display.pack(fill="both", padx=20, pady=(30, 15))

        # Main frame for the calculator buttons
        button_frame = tk.Frame(root, bg="#121212")
        button_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Layout mapping: (text, row, col, rowspan, columnspan, bg_color, fg_color, active_bg)
        buttons_layout = [
            # Row 0: Scientific & Utility Functions
            ("INV", 0, 0, 1, 1, "#2c2c2c", "white", "#4a4a4a"),
            ("RAD", 0, 1, 1, 1, "#2c2c2c", "white", "#4a4a4a"),
            ("x!", 0, 2, 1, 1, "#2c2c2c", "white", "#4a4a4a"),
            ("(", 0, 3, 1, 1, "#2c2c2c", "white", "#4a4a4a"),
            (")", 0, 4, 1, 1, "#2c2c2c", "white", "#4a4a4a"),
            # Row 1: Trigonometric & Logarithmic Functions
            ("sin", 1, 0, 1, 1, "#2c2c2c", "white", "#4a4a4a"),
            ("cos", 1, 1, 1, 1, "#2c2c2c", "white", "#4a4a4a"),
            ("tan", 1, 2, 1, 1, "#2c2c2c", "white", "#4a4a4a"),
            ("log", 1, 3, 1, 1, "#2c2c2c", "white", "#4a4a4a"),
            ("ln", 1, 4, 1, 1, "#2c2c2c", "white", "#4a4a4a"),
            # Row 2: Powers, Constants & Roots
            ("x²", 2, 0, 1, 1, "#2c2c2c", "white", "#4a4a4a"),
            ("x^y", 2, 1, 1, 1, "#2c2c2c", "white", "#4a4a4a"),
            ("π", 2, 2, 1, 1, "#2c2c2c", "white", "#4a4a4a"),
            ("e", 2, 3, 1, 1, "#2c2c2c", "white", "#4a4a4a"),
            ("√", 2, 4, 1, 1, "#2c2c2c", "white", "#4a4a4a"),
            # Row 3: Clear, Percentage, Backspace & Division (spanning 2 columns)
            ("AC", 3, 0, 1, 1, "#4a4a4a", "white", "#686868"),
            ("%", 3, 1, 1, 1, "#4a4a4a", "white", "#686868"),
            ("⌫", 3, 2, 1, 1, "#4a4a4a", "white", "#686868"),
            ("÷", 3, 3, 1, 2, "#5c5c5c", "white", "#828282"),
            # Row 4: Numbers 7, 8, 9 & Multiplication
            ("7", 4, 0, 1, 1, "#2c2c2c", "white", "#4a4a4a"),
            ("8", 4, 1, 1, 1, "#2c2c2c", "white", "#4a4a4a"),
            ("9", 4, 2, 1, 1, "#2c2c2c", "white", "#4a4a4a"),
            ("×", 4, 3, 1, 2, "#5c5c5c", "white", "#828282"),
            # Row 5: Numbers 4, 5, 6 & Subtraction
            ("4", 5, 0, 1, 1, "#2c2c2c", "white", "#4a4a4a"),
            ("5", 5, 1, 1, 1, "#2c2c2c", "white", "#4a4a4a"),
            ("6", 5, 2, 1, 1, "#2c2c2c", "white", "#4a4a4a"),
            ("-", 5, 3, 1, 2, "#5c5c5c", "white", "#828282"),
            # Row 6: Numbers 1, 2, 3 & Addition
            ("1", 6, 0, 1, 1, "#2c2c2c", "white", "#4a4a4a"),
            ("2", 6, 1, 1, 1, "#2c2c2c", "white", "#4a4a4a"),
            ("3", 6, 2, 1, 1, "#2c2c2c", "white", "#4a4a4a"),
            ("+", 6, 3, 1, 2, "#5c5c5c", "white", "#828282"),
            # Row 7: Zero, Decimal Point & Equal Sign
            ("0", 7, 0, 1, 2, "#2c2c2c", "white", "#4a4a4a"),
            (".", 7, 2, 1, 1, "#2c2c2c", "white", "#4a4a4a"),
            ("=", 7, 3, 1, 1, "#ff9500", "white", "#ffb13b"),
            (" ", 7, 4, 1, 1, "#121212", "#121212", "#121212"),  # Spacer
        ]

        # Render all buttons dynamically based on layout specifications
        for (
            text,
            row,
            col,
            r_span,
            c_span,
            bg_color,
            fg_color,
            active_bg,
        ) in buttons_layout:
            action = lambda x=text: self.on_button_click(x)

            btn = tk.Button(
                button_frame,
                text=text,
                font=("Arial", 15, "bold"),
                bg=bg_color,
                fg=fg_color,
                activebackground=active_bg,
                activeforeground="white" if fg_color != "#121212" else "#121212",
                relief="flat",
                bd=0,
                command=action,
            )

            btn.grid(
                row=row,
                column=col,
                rowspan=r_span,
                columnspan=c_span,
                sticky="nsew",
                padx=4,
                pady=4,
            )

        # Configure uniform resizing weights for 8 rows and 5 columns
        for i in range(8):
            button_frame.grid_rowconfigure(i, weight=1)
        for j in range(5):
            button_frame.grid_columnconfigure(j, weight=1)

        # Bind PC keyboard events for seamless desktop experience
        self.root.bind("<Key>", self.handle_keypress)

    def handle_keypress(self, event):
        """Allows direct keyboard input for desktop users."""
        key = event.char
        if key in "0123456789+-().*%/":
            if key == "*":
                self.on_button_click("×")
            elif key == "/":
                self.on_button_click("÷")
            else:
                self.on_button_click(key)
        elif event.keysym in ["Return", "KP_Enter"]:
            self.on_button_click("=")
        elif event.keysym == "BackSpace":
            self.on_button_click("⌫")
        elif event.keysym in ["Escape", "c", "C"]:
            self.on_button_click("AC")

    def on_button_click(self, char):
        """Handles calculator logic, conversions, and evaluations."""
        if char.strip() == "":
            return

        if char == "AC":
            self.display.delete(0, tk.END)
        elif char == "⌫":
            current = self.display.get()
            if current:
                self.display.delete(len(current) - 1, tk.END)
        elif char == "x^y":
            self.display.insert(tk.END, "^")
        elif char == "x²":
            self.display.insert(tk.END, "**2")
        elif char == "=":
            try:
                expression = (
                    self.display.get()
                    .replace("×", "*")
                    .replace("÷", "/")
                    .replace("π", str(math.pi))
                    .replace("e", str(math.e))
                    .replace("^", "**")
                )
                result = eval(expression)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif char in ["sin", "cos", "tan", "log", "ln", "√", "x!"]:
            try:
                val = float(self.display.get())
                if char == "sin":
                    res = math.sin(math.radians(val))
                elif char == "cos":
                    res = math.cos(math.radians(val))
                elif char == "tan":
                    res = math.tan(math.radians(val))
                elif char == "log":
                    res = math.log10(val)
                elif char == "ln":
                    res = math.log(val)
                elif char == "√":
                    res = math.sqrt(val)
                elif char == "x!":
                    res = math.factorial(int(val))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(res))
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, char)


if __name__ == "__main__":
    root = tk.Tk()
    calc = ScientificCalculator(root)
    root.mainloop()