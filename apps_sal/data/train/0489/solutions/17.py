class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        # sorting sol O(nlgn)
        arr = [(a, i) for i, a in enumerate(A)]
        arr.sort()
        # # first way is keep imin, start from left of arr
        # imin, res = float('inf'), 0
        # for _, i in arr:
        #     res = max(res, i-imin)
        #     imin = min(imin, i)
        # return res

        # second way is keep imax, start from right of arr
        imax, res = float('-inf'), 0
        for _, i in reversed(arr):
            res = max(res, imax - i)
            imax = max(imax, i)
        return res
