class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        N = len(A)
        if K == 1 or N == 1:
            return sum(A)

        dp = [0] * (N + 1)
        dp[0] = 0
        for i in range(N):
            mv = A[i]
            dp[i + 1] = dp[i] + A[i]
            for j in range(1, min(i + 1, K)):
                mv = max(mv, A[i - j])
                dp[i + 1] = max(dp[i + 1], dp[i - j] + (j + 1) * mv)

        return dp[N]
