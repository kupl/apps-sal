class Solution:

    def findBestValue(self, arr: List[int], target: int) -> int:
        l = 0
        r = max(arr)
        while l < r:
            mid = (l + r) // 2 + 1
            if sum((min(e, mid) for e in arr)) > target:
                r = mid - 1
            else:
                l = mid
        if abs(sum((min(e, l) for e in arr)) - target) <= abs(sum((min(e, l + 1) for e in arr)) - target):
            return l
        else:
            return l + 1
