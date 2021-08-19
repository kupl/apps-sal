class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        for a in arr:
            dp[a] = dp.get(a - difference, 0) + 1
        return max(dp.values())
