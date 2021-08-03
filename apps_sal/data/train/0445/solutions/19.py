class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:  # if only one number is left difference is 0
            return 0
        nums.sort()
        return min(nums[-1 - i] - nums[3 - i] for i in range(4))
        # nums[-1 -0/1/2/3] is getting the largest 4 numbers
        # nums[3 - 0/1/2/3] is getting the smallest 4 numbers
