class Solution:

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        n = len(A)
        dp = [0] * (n + 1)
        for (i, a) in enumerate(A, 1):
            for j in range(1, K + 1):
                if i - j >= 0:
                    dp[i] = max(dp[i], dp[i - j] + max(A[i - j:i]) * j)
        return dp[-1]
