class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        expression = list(expression)

        def replace(start: int, logical: str):
            braket = 1
            idxs = []
            for i in range(start, len(expression)):
                if expression[i] == '(':
                    braket += 1
                elif expression[i] == ')':
                    braket -= 1
                elif braket == 1 and expression[i] == ',':
                    idxs.append(i)
                elif braket == 0:
                    break

            for i in idxs:
                expression[i] = logical

        for idx, char in enumerate(expression):
            if char == '|':
                expression[idx] = ''
                replace(idx + 2, 'or')
            elif char == '&':
                expression[idx] = ''

        expr = ' '.join(expression).replace('t', 'True').replace('f', 'False').replace('!', 'not').replace(',', 'and')

        return eval(expr)
