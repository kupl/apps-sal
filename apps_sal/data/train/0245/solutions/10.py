class Solution:
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) < 2:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0]) + '/' + str(nums[1])
        l = str(nums[0]) + '/('
        for x in nums[1:]:
            l = l + str(x) + '/'
        return l[:-1] + ')'
