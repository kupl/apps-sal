class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        a = len(arr)
        dp = {}
        ans = 0
        for value in arr:
            targetValue = value - difference
            if targetValue in dp:
                dp[value] = 1 + dp[targetValue]
            else:
                dp[value] = 1
            ans = max(ans, dp[value])
        return ans
