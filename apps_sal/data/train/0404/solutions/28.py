class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:

        N = len(A)
        pre_sum = [0 for i in range(N)]
        pre_sum[0] = A[0]

        for j in range(1, len(A)):

            pre_sum[j] = pre_sum[j - 1] + A[j]

        dp = [[0 for n in range(N)] for k in range(K + 1)]

        for i in range(N):

            dp[1][i] = pre_sum[i] / (i + 1)

        for k in range(2, K + 1):

            for i in range(N):

                for j in range(i):

                    dp[k][i] = max(dp[k][i], pre_sum[i] / (i + 1), dp[k - 1][j] + (pre_sum[i] - pre_sum[j]) / (i - j))

        return dp[K][N - 1]
