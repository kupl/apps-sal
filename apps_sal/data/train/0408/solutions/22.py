

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        def helper(num):
            new_sum = sum([num if i > num else i for i in arr])
            return new_sum

        left, right = 0, max(arr)
        while left < right:
            mid = left + (right - left) // 2
            if helper(mid) < target:
                left = mid + 1
            elif helper(mid) >= target:
                right = mid

        if abs(helper(left) - target) < abs(helper(left - 1) - target):
            return left
        else:
            return left - 1
