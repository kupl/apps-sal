class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        l, r, res = 0, 1, 1
        while r < len(A):
            c = A[r-1] - A[r] 
            if c == 0:
                l = r
            elif r == len(A)-1 or c*(A[r] - A[r+1]) >= 0:
                res = max(res, r-l+1)
                l = r
            r += 1
        return res
