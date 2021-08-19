class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0
        nums.sort()
        # remove smallest 3
        min_diff = nums[-1] - nums[3]

        for i in range(3):
            min_diff = min(min_diff, nums[-2 - i] - nums[3 - i - 1])

        return min_diff
