class Solution:

    def getMaxLen(self, A: List[int]) -> int:
        n = len(A)
        lastZ = -1
        lastN = n
        cur = 1
        res = 0
        for (i, a) in enumerate(A):
            cur *= a
            if cur == 0:
                lastZ = i
                lastN = n
                cur = 1
            elif cur > 0:
                res = max(res, i - lastZ)
            else:
                lastN = min(lastN, i)
                res = max(res, i - lastN)
        return res
