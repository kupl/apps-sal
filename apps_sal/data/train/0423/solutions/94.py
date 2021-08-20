class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        ans = 1
        for i in range(len(arr)):
            count = 1
            if arr[i] - difference in dp:
                count += dp[arr[i] - difference]
            dp[arr[i]] = count
            ans = max(ans, count)
        return ans
