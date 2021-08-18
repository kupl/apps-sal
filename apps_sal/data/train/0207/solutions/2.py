class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        maxPos = 0
        maxNum = ''
        res = ''
        while nums:
            for i in range(len(nums)):
                cur = nums[i]
                if str(cur) + maxNum >= maxNum + str(cur):
                    maxNum = str(cur)
                    maxPos = i
            nums.pop(maxPos)
            res += maxNum
            maxPos = 0
            maxNum = ''
        if res[0] == '0':
            return '0'
        return res
