class Solution:

    def satisfyThreshold(self, nums, threshold, divisor):
        return sum(((n - 1) // divisor + 1 for n in nums)) <= threshold

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        while left < right:
            mid = left + (right - left) // 2
            if self.satisfyThreshold(nums, threshold, mid):
                right = mid
            else:
                left = mid + 1
        return left
