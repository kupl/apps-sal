class Solution:

    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        dp = {}
        for i in arr:
            if i - diff in dp:
                dp[i] = dp[i - diff] + 1
            else:
                dp[i] = 1
        return max(dp.values())
