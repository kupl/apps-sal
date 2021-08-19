class Solution:

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect
        d = [0] * len(nums)
        maxLen = 0
        for n in nums:
            i = bisect.bisect_left(d, n, 0, maxLen)
            if i == maxLen:
                maxLen += 1
            d[i] = n
        return maxLen
