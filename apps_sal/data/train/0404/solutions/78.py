class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        dp = [[0] * K for _ in range(n)]
        dp[0][0] = A[0]
        for i in range(1, n):
            dp[i][0] = (dp[i - 1][0] * i + A[i]) / (i + 1)
        for k in range(1, K):
            for i in range(k, n):
                curr_sum = 0
                for j in reversed(range(k, i + 1)):
                    curr_sum += A[j]
                    dp[i][k] = max(dp[i][k], dp[j - 1][k - 1] + curr_sum / (i + 1 - j))
        return dp[n - 1][K - 1]
