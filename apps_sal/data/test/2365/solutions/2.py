from functools import reduce


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def parse_or(*l):
            return reduce(lambda x, y: x or y, l)

        def parse_and(*l):
            return reduce(lambda x, y: x and y, l)

        def parse_not(x):
            return not x

        expression = expression.replace('t', 'True')
        expression = expression.replace('f', 'False')

        expression = expression.replace('|', 'parse_or')
        expression = expression.replace('&', 'parse_and')
        expression = expression.replace('!', 'parse_not')

        return eval(expression)
