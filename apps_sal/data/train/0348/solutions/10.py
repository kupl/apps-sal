class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        max1: int = arr[0]
        max0: int = arr[0]
        res: int = arr[0]
        for a in arr[1:]:
            max1 = max(max1 + a, max0, a)
            max0 = max(max0 + a, a)
            res = max(res, max1)
        return res
