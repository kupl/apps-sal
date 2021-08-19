class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        max_len = 1
        dp = {}
        for a in arr:
            if a - difference in dp:
                dp[a] = dp[a - difference] + 1
                max_len = max(max_len, dp[a])
            else:
                dp[a] = 1
        return max_len
