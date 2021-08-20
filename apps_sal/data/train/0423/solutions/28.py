class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        maxs = 1
        for num in arr:
            dp[num] = dp.get(num - difference, 0) + 1
            if dp[num] > maxs:
                maxs = dp[num]
        return maxs
