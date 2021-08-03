class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # maxPos = 0
        # maxNum = ''
        # maxLen = 0
        # maxCut = ''
        # res = ''
        # while nums:
        #     for i in range(len(nums)):
        #         cur = nums[i]
        #         ori = cur
        #         while cur % 10 == 0:
        #             cur = cur // 10
        #         if str(cur) > maxCut or (str(cur) == maxCut and len(str(ori)) < maxLen):
        #             maxCut = str(cur)
        #             maxNum = str(ori)
        #             maxPos = i
        #             maxLen = len(maxNum)
        #     nums.pop(maxPos)
        #     res += maxNum
        #     maxPos = 0
        #     maxNum = ''
        #     maxLen = 0
        #     maxCut = ''
        # return res

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
