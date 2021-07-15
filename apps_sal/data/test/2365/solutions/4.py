class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        return eval(expression.translate(str.maketrans({'t': '1', 'f': '0', '!': 'not', '|': 'or_', '&': 'and_'})), {'or_': lambda *a: any(a), 'and_': lambda *a: all(a)})

