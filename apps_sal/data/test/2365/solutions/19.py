class Solution:
    def parseBoolExpr(self, ex: str) -> bool:
        def recur(i):
            if ex[i] in ('t', 'f'):
                return True if ex[i] == 't' else False, i + 1
            op = ex[i]
            i, stack = i + 2, []
            while ex[i] != ')':
                if ex[i] == ',':
                    i += 1
                    continue
                res, i = recur(i)
                stack.append(res)
            if op == '&':
                return all(stack), i + 1
            elif op == '|':
                return any(stack), i + 1
            elif op == '!':
                return not stack[0], i + 1
            return res, i + 1

        return recur(0)[0]
