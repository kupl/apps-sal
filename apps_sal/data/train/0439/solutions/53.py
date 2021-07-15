class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        inc = 1
        dec = 1
        res = 1
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                inc, dec = dec + 1, 1
                res = max(res, inc)
            elif A[i] < A[i-1]:
                inc, dec = 1, inc + 1
                res = max(res, dec)
            else:
                inc, dec = 1, 1
        return res
