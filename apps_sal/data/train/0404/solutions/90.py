class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        dp = [[0] * (n + 1) for _ in range(K + 1)]
        sums = [0] * (n + 1)
        for i in range(1, n + 1):
            sums[i] = sums[i - 1] + A[i - 1]
            dp[1][i] = sums[i] / i
        for k in range(2, K + 1):
            for i in range(k, n + 1):
                for j in range(k - 1, i):
                    dp[k][i] = max(dp[k][i], dp[k - 1][j] + (sums[i] - sums[j]) / (i - j))
        return dp[K][n]

