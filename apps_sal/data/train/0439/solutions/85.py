class Solution:

    def maxTurbulenceSize(self, A: List[int]) -> int:
        (res, l, b, log) = (1, 1, A[0], -1)
        for a in A[1:]:
            if a == b:
                (log, l) = (-1, 1)
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
            (res, b) = (max(res, l), a)
        return res
