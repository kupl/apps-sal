class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        sums = [0 for i in range(n + 1)]
        dp = [[0 for i in range(n + 1)] for k in range(K + 1)]
        for i in range(1, n + 1):
            sums[i] += sums[i - 1] + A[i - 1]
        for i in range(1, n + 1):
            dp[1][i] = sums[i] / i
        for k in range(2, K + 1):
            for i in range(n + 1):
                for j in range(i):
                    dp[k][i] = max(dp[k][i], dp[k - 1][j] + (sums[i] - sums[j]) / (i - j))
        return dp[K][n]
