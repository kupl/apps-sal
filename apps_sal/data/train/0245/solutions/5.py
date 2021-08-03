class Solution:
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        res = ''

        if len(nums) == 1:
            return str(nums[0])

        if len(nums) == 2:
            return str(nums[0]) + '/' + str(nums[1])

        for i in range(0, len(nums)):
            if i == 0:
                res = res + str(nums[i]) + '/('
            elif i < len(nums) - 1:
                res = res + str(nums[i]) + '/'
            else:
                res = res + str(nums[i]) + ')'
        return res
