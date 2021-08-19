class Solution:

    def parseBoolExpr(self, expression: str) -> bool:
        expression = list(expression)
        table = {'|': 'or', '&': 'and', 't': 'True', 'f': 'False'}
        logic = []
        (idx, par) = (0, True)
        while idx < len(expression):
            if expression[idx] in ['&', '|']:
                logic.append(table[expression[idx]])
                expression[idx] = ''
                idx += 2
            elif expression[idx] == '!':
                logic.append('not')
                expression[idx] = 'not'
                idx += 2
            else:
                if not par and logic:
                    logic.pop()
                    par = True
                if expression[idx] in ['t', 'f']:
                    expression[idx] = table[expression[idx]]
                elif expression[idx] == ',':
                    expression[idx] = logic[-1]
                elif expression[idx] == ')':
                    if logic[-1] == 'not':
                        logic.pop()
                    else:
                        par = False
                idx += 1
        return eval(' '.join(expression))
