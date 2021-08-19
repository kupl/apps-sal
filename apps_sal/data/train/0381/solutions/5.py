class Solution:

    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < s:
            return 0
        res = float('inf')
        start = 0
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            while curr >= s:
                res = min(res, i - start + 1)
                curr -= nums[start]
                start += 1
        return res
