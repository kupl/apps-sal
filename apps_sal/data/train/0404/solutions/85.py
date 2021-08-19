class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        A = [0] + A
        dp = [[0] * (K + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            dp[i][0] = -float('inf')
        for i in range(1, n + 1):
            for k in range(1, min(i + 1, K + 1)):
                sum_s = 0
                for j in range(i, k - 1, -1):
                    sum_s += A[j]
                    dp[i][k] = max(dp[i][k], dp[j - 1][k - 1] + sum_s / (i - j + 1))
        res = 0
        for i in range(1, K + 1):
            res = max(res, dp[n][i])
        return res
