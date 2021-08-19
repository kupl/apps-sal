class Solution:

    def largestSumOfAverages(self, A, K):
        m = len(A)
        dp = [[None] * (K + 1) for _ in range(m)]
        for k in range(1, K + 1):
            for j in range(k - 1, m):
                if k == 1:
                    dp[j][k] = sum(A[:j + 1]) / (j + 1)
                else:
                    dp[j][k] = max((dp[i][k - 1] + sum(A[i + 1:j + 1]) / (j - i) for i in range(k - 2, j)))
        return dp[-1][-1]
