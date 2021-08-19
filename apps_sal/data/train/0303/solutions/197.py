class Solution:

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        N = len(arr)
        dp = [0] * (N + 1)
        for i in range(N):
            curMax = 0
            for j in range(1, min(k, i + 1) + 1):
                curMax = max(curMax, arr[i - j + 1])
                dp[i] = max(dp[i], dp[i - j] + curMax * j)
        return dp[N - 1]
