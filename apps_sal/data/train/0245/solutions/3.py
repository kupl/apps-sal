class Solution:
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        n = len(nums)
        if n == 1:
            return str(nums[0])
        elif n == 2:
            return str(nums[0]) + '/' + str(nums[1])
        else:
            result = str(nums[0]) + '/('
            for i in range(1, n - 1):
                result += str(nums[i]) + '/'
            result += str(nums[-1]) + ')'
            return result
