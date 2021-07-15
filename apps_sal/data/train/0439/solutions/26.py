class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        res = 1
        l = 1
        b = A[0]
        log = -1
        for a in A[1:]:
            if a == b:
                log = -1
                l = 1
            elif a > b:
                if log != 1:
                    l += 1
                else:
                    l = 2
                log = 1
            else:
                if log != 0:
                    l += 1
                else:
                    l = 2
                log = 0
            res = max(res, l)
            b = a
        return res

