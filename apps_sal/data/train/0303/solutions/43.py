class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        L = len(arr)
        dp = [0] * L
        for i in range(k):
            dp[i] = max(arr[:i + 1]) * (i + 1)
        for i in range(k, L):
            dp[i] = dp[i - k] + max(arr[i - k + 1:i + 1]) * k
            for j in range(1, k):
                dp[i] = max(dp[i], dp[i - j] + max(arr[i - j + 1:i + 1]) * j)
        return dp[-1]
