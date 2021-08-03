class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 3:
            return 0

        nums.sort()
        return min(nums[n - 4 + i] - nums[i] for i in range(4))
