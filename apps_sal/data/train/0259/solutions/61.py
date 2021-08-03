from math import ceil


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        while left <= right:
            m = left + (right - left) // 2
            if self.check(nums, m, threshold):
                ans = m
                right = m - 1
            else:
                left = m + 1
        return ans

    def check(self, nums, m, threshold):
        return sum([ceil(x / m) for x in nums]) <= threshold
