class Solution:

    def optimalDivision(self, nums):
        if len(nums) == 1:
            return str(nums[0]) + ''
        elif len(nums) == 2:
            return str(nums[0]) + '/' + str(nums[1])
        answer = str(nums[0]) + '/(' + str(nums[1])
        for i in nums[2:]:
            answer += '/' + str(i)
        answer += ')'
        return answer
