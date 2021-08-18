class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        N = len(A)
        dp = [float('-inf')] * (N + 1)
        for i in range(1, N + 1):
            if i <= K:
                dp[i] = max(A[:i]) * i
            else:
                for j in range(1, K + 1):
                    dp[i] = max(dp[i], dp[i - j] + max(A[i - j:i]) * j)
        return dp[-1]
