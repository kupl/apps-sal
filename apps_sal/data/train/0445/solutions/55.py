class Solution:

    def minDifference(self, nums: List[int]) -> int:
        l = len(nums)
        if l < 5:
            return 0
        nums.sort()
        min = 99999999999
        if min > nums[l - 1] - nums[3]:
            min = nums[l - 1] - nums[3]
        if min > nums[l - 2] - nums[2]:
            min = nums[l - 2] - nums[2]
        if min > nums[l - 3] - nums[1]:
            min = nums[l - 3] - nums[1]
        if min > nums[l - 4] - nums[0]:
            min = nums[l - 4] - nums[0]
        return min
