class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        dp, ans = dict(), 0
        for i in arr:
            dp[i] = dp.get(i - diff, 0) + 1
            ans = max(ans, dp[i])
        return ans
