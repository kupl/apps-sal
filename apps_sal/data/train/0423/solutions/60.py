class Solution:
    def longestSubsequence(self, arr: List[int], diff: int) -> int:
        n = len(arr)
        dp = dict()
        for i in range(n):
            if arr[i] - diff in dp:
                if arr[i] in dp:
                    dp[arr[i]] = max(dp[arr[i]], dp[arr[i] - diff] + 1)
                else:
                    dp[arr[i]] = dp[arr[i] - diff] + 1
            else:
                if arr[i] in dp:
                    dp[arr[i]] = max(dp[arr[i]], 1)
                else:
                    dp[arr[i]] = 1
        return max(dp.values())
