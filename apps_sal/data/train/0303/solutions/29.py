class Solution:

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        dp = [0] * len(A)
        for i in range(K):
            dp[i] = max(A[:i + 1]) * (i + 1)
        for i in range(K, len(A)):
            dp[i] = max([dp[i - j] + max(A[i - j + 1:i + 1]) * j for j in range(1, K + 1)])
        return dp[-1]
