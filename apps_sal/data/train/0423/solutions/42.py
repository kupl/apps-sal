class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        n = len(arr)
        ans = 0
        for i in range(n):
            if arr[i] - difference in dp:
                dp[arr[i]] = dp[arr[i] - difference] + 1
            else:
                dp[arr[i]] = 1
            ans = max(ans, dp[arr[i]])

        return ans
