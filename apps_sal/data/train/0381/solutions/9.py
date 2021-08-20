class Solution(object):

    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        import math
        minlen = math.inf
        pt1 = 0
        pt2 = 0
        cursum = nums[0]
        while pt2 < len(nums):
            if cursum >= s:
                minlen = min(minlen, pt2 - pt1 + 1)
            if minlen == 1:
                return 1
            if cursum < s:
                pt2 += 1
                if pt2 < len(nums):
                    cursum += nums[pt2]
            elif cursum >= s:
                cursum -= nums[pt1]
                pt1 += 1
        return 0 if minlen == math.inf else minlen
