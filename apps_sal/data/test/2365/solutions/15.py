class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def parse(e: str, left, right):
            if right - left == 1:
                return e[left] == 't'
            res = e[left] == '&'  # only when the first char is '&', ans assigned True.
            level, start = 0, left + 2  # e[left + 1] must be '(', so start from lo + 2 to delimit sub-expression.
            for i in range(left + 2, right):
                if level == 0 and e[i] in [',', ')']:  # found a sub-expression.
                    cur = parse(e, start, i)
                    start = i + 1
                    if e[left] == '&':
                        res &= cur
                    elif e[left] == '|':
                        res |= cur
                    else:  # e[lo] is '!'.
                        res = not cur
                if e[i] == '(':
                    level = level + 1
                elif e[i] == ')':
                    level = level - 1
            return res

        return parse(expression, 0, len(expression))
