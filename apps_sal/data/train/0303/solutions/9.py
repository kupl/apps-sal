class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        n = len(A)
        dp = [0] * (n + 1)
        for i in range(n):
            curMax = 0
            for k in range(1, min(K, i + 1) + 1):
                curMax = max(curMax, A[i - k + 1])
                dp[i] = max(dp[i], dp[i - k] + curMax * k)

        print(dp)
        return dp[n - 1]
