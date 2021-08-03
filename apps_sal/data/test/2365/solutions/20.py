class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        ops = {'!', '&', '|'}

        def parse(start):
            if expression[start] == 'f':
                return False, start + 1
            if expression[start] == 't':
                return True, start + 1
            if expression[start] in ops:
                new_start = start + 2
                vals = set()
                while new_start < len(expression):
                    val, new_start = parse(new_start)
                    vals.add(val)
                    if expression[new_start] == ')':
                        new_start += 1
                        break
                    assert expression[new_start] == ','
                    new_start += 1
                if expression[start] == '!':
                    assert len(vals) == 1
                    return not list(vals)[0], new_start
                if expression[start] == '&':
                    return all(vals), new_start
                return any(vals), new_start

        return parse(0)[0]
