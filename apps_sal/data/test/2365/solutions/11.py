class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        table = {'|': 'or', '&': 'and', 't': 'True', 'f': 'False', '(': '('}

        expr, logic = [], []
        idx, par = 0, True
        while idx < len(expression):
            if expression[idx] in ['&', '|']:
                logic.append(table[expression[idx]])
            elif expression[idx] == '!':
                logic.append('not')
                expr.append('not')
            else:
                if not par and logic:
                    logic.pop()
                    par = True

                if expression[idx] in ['t', 'f', '(']:
                    expr.append(table[expression[idx]])
                elif expression[idx] == ',':
                    expr.append(logic[-1])
                elif expression[idx] == ')':
                    expr.append(')')
                    if logic[-1] == 'not':
                        logic.pop()
                    else:
                        par = False

            idx += 1

        return eval(' '.join(expr))

