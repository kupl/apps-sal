class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        res = 0
        for num in arr:
            dp[num] = 1 + dp.get(num - difference, 0)
            res = max(res, dp[num])
        return res
