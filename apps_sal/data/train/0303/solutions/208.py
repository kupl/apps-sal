class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        N = len(arr)
        K = k
        dp = [0] * (N + 1)
        for i in range(N):
            curMax = 0
            for k in range(1, min(K, i + 1) + 1):
                curMax = max(curMax, arr[i - k + 1])
                dp[i] = max(dp[i], dp[i - k] + curMax * k)
        return dp[N - 1]
                

