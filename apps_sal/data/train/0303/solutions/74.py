class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        n = len(A)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            for j in range(1, K + 1):
                if i - j >= 0:
                    m = max(A[i - j:i])
                    dp[i] = max(dp[i], dp[i - j] + m * j)
        return dp[-1]
