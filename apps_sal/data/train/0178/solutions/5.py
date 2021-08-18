class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [float('inf')] * (n + 1)
        res = 0

        for num in nums:
            lo, hi = 1, n
            while lo < hi:
                mi = int((lo + hi) / 2)
                if dp[mi] < num:
                    lo = mi + 1
                else:
                    hi = mi
            dp[lo] = num
            res = max(res, lo)
        return res
