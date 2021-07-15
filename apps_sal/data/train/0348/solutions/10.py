class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        max1: int = arr[0]  # max subarray sum with at most one deletion
        max0: int = arr[0]  # max subarray sum with NO deletion
        res: int = arr[0]  # overall max to be returned
        for a in arr[1:]:
            max1 = max(max1 + a, max0, a)  # include a, not include a, or start with a
            max0 = max(max0 + a, a)  # update `max0`
            res = max(res, max1)  # update overall max
        return res
