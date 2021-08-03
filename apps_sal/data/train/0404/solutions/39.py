class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        dp = [[0] * n for _ in range(K)]
        # dp: K*n, dp[k][i]: result for largestSum of first (i+1) elements with k+1 groups
        for i in range(n):
            dp[0][i] = sum(A[:(i + 1)]) / (i + 1)
        for l in range(1, K):
            for i in range(l, n):
                for j in range(i):
                    dp[l][i] = max(dp[l][i], dp[l - 1][j] + sum(A[j + 1:i + 1]) / (i - j))
        return dp[K - 1][n - 1]
