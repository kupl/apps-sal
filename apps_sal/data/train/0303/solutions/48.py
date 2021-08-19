class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * len(arr)
        for i in range(k):
            dp[i] = max(arr[:i + 1]) * (i + 1)
        for i in range(k, len(arr)):
            for j in range(1, k + 1):
                dp[i] = max(dp[i], dp[i - j] + max(arr[i - j + 1:i + 1]) * j)
        return dp[-1]
