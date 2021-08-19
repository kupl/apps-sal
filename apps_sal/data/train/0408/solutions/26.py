class Solution:

    def findBestValue(self, arr: List[int], target: int) -> int:
        (left, right) = (0, max(arr))
        while left <= right:
            mid = left + right >> 1
            count = sum([min(x, mid) for x in arr])
            if count < target:
                left = mid + 1
            else:
                right = mid - 1
        res1 = sum([min(x, left) for x in arr])
        res2 = sum([min(x, right) for x in arr])
        return left if abs(res1 - target) < abs(res2 - target) else right
