class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        dp = [[0 for _ in range(K + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for k in range(1, K + 1):
                if k == 1:
                    dp[i][k] = sum(A[:i]) / i
                else:
                    for j in range(k, i + 1):
                        dp[i][k] = max(dp[i][k], dp[j - 1][k - 1] + sum(A[j - 1:i]) / (i - j + 1))
        return dp[n][K]
