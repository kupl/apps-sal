class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        arr = [(a, i) for i, a in enumerate(A)]
        arr.sort()

        imax, res = float('-inf'), 0
        for _, i in reversed(arr):
            res = max(res, imax - i)
            imax = max(imax, i)
        return res
