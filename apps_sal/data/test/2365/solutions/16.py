from functools import reduce


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        operations = {
            '|': any,
            '&': all,
            '!': lambda x: not x[0]
        }

        def getTokens(expression):
            depth = 0
            token = ''
            for s in expression:
                if s == ',' and depth == 0:
                    yield token
                    token = ''
                    continue
                if s == '(':
                    depth += 1
                elif s == ')':
                    depth -= 1
                token += s

            yield token

        def evaluate(expression):
            if expression == 't':
                return True
            elif expression == 'f':
                return False

            operator = operations[expression[0]]
            values = [evaluate(token) for token in getTokens(expression[2:-1])]
            return operator(values)

        return evaluate(expression)
