class Solution:

    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0
        nums = sorted(nums)
        print(nums)
        n = len(nums) - 1
        return min(nums[n] - nums[3], nums[n - 1] - nums[2], nums[n - 2] - nums[1], nums[n - 3] - nums[0])
