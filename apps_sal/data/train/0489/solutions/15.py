class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        arr = [(a, i) for i, a in enumerate(A)]
        arr.sort()
        imin, res = float('inf'), 0
        for _, i in arr:
            res = max(res, i - imin)
            imin = min(imin, i)
        return res
