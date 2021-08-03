class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        dp = [0 for i in range(len(A) + 1)]
        for i in range(1, len(A) + 1):
            dp[i] = max([dp[i - j] + j * max(A[i - j:i]) for j in range(1, K + 1) if j <= i])
        print(dp)
        return dp[-1]
