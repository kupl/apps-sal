class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        max_len = 1
        for num in arr:
            dp[num] = max(dp.get(num, 1), 1 + dp.get(num - difference, 0))
            max_len = max(max_len, dp[num])
        return max_len
