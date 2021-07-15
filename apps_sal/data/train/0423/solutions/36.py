class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp, res = {}, 0
        for i in arr:
            dp[i] = dp.get(i-difference, 0) + 1
            res = max(res, dp[i])
        return res
