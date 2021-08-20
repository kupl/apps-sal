class Solution:

    def queryString(self, S: str, N: int) -> bool:
        if '1' not in S:
            return False
        res = set()
        cur = set()
        for s in S:
            if s == '0':
                cur = {c * 2 for c in cur} | {0}
            else:
                cur = {c * 2 + 1 for c in cur} | {1}
            res |= cur
        for i in range(1, N + 1):
            if i not in res:
                return False
        return True
