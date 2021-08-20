class Solution:

    def parseBoolExpr(self, expression: str) -> bool:
        bool_stack = []
        expr_stack = []
        curr = []
        for char in expression:
            if char == ',':
                continue
            elif char == '(':
                expr_stack.append(curr)
                curr = []
            elif char in 'tf':
                curr.append(True if char == 't' else False)
            elif char in '|&!':
                bool_stack.append(char)
            else:
                b = bool_stack.pop()
                prev = expr_stack.pop() if expr_stack else []
                if b == '!':
                    curr = prev + [not curr.pop()]
                elif b == '&':
                    curr = prev + [all(curr)]
                else:
                    curr = prev + [any(curr)]
        return curr.pop()
