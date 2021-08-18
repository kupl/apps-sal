class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def parse(e: str, left, right):
            if right - left == 1:
                return e[left] == 't'
            res = e[left] == '&'
            level, start = 0, left + 2
            for i in range(left + 2, right):
                if level == 0 and e[i] in [',', ')']:
                    cur = parse(e, start, i)
                    start = i + 1
                    if e[left] == '&':
                        res &= cur
                    elif e[left] == '|':
                        res |= cur
                    else:
                        res = not cur
                if e[i] == '(':
                    level = level + 1
                elif e[i] == ')':
                    level = level - 1
            return res

        return parse(expression, 0, len(expression))
