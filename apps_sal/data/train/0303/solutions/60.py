class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        if not A:
            return 0
        N = len(A)
        if K == N:
            return N * max(A)
        dp = [0 for i in range(N)]
        for i in range(K):
            dp[i] = max(A[:i + 1]) * (i + 1)
        for i in range(K, N):
            a = max(A[i - K + 1:i + 1])
            dp[i] = max([dp[i - j] + j * max(A[i - j + 1:i + 1]) for j in range(1, K + 1)])
        return dp[-1]
