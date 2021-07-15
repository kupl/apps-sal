class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        expression = list(expression)

        def replace_or(start: int):
            braket = 1
            for i in range(start, len(expression)):
                if expression[i] == '(':
                    braket += 1
                elif expression[i] == ')':
                    braket -= 1
                elif braket == 1 and expression[i] == ',':
                    expression[i] = 'or'
                elif braket == 0:
                    break

        for idx, char in enumerate(expression):
            if char == '|':
                expression[idx] = ''
                replace_or(idx + 2)
            elif char == '&':
                expression[idx] = ''
            elif char == 't':
                expression[idx] = 'True'
            elif char == 'f':
                expression[idx] = 'False'
            elif char == '!':
                expression[idx] = 'not'

        expr = ' '.join(expression).replace(',', 'and')

        return eval(expr)

