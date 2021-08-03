class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        N = len(A)
        DP = [0] * (N + 1)
        for i in range(N):
            curMax = 0
            for k in range(1, min(K, i + 1) + 1):
                curMax = max(curMax, A[i - k + 1])
                DP[i] = max(DP[i], DP[i - k] + curMax * k)
        return DP[N - 1]
