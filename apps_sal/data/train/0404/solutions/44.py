class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        dp = [[0 for k in range(K)] for i in range(n)]
        for k in range(K):
            dp[0][k] = A[0]
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0] * i / (i + 1) + A[i] / (i + 1)
        for k in range(1, K):
            for i in range(1, n):
                for j in range(i):
                    dp[i][k] = max(dp[i][k], dp[j][k - 1] + sum(A[j + 1:i + 1]) / (i - j))
        return dp[n - 1][K - 1]
