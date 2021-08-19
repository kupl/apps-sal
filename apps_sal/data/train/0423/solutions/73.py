class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        res = 1
        for i in arr:
            comp = i - difference
            if comp in dp:
                dp[i] = dp[comp] + 1
                res = max(res, dp[i])
            else:
                dp[i] = 1
        return res
