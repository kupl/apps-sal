class Solution:
    def optimalDivision(self, nums):
        nums = list(map(str, nums))
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return "/".join(nums)
        nums[1] = '(' + nums[1]
        nums[-1] = nums[-1] + ')'
        return "/".join(nums)
