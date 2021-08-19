class Solution:

    def largestSumOfAverages(self, A, K: int) -> float:

        def avg(array):
            return sum(array) / len(array)
        dp = [[0 for _ in range(K + 1)] for _ in range(len(A))]
        means = [[0 for _ in range(len(A))] for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(i, len(A)):
                means[i][j] = avg(A[i:j + 1])
        for i in range(len(A)):
            dp[i][1] = means[0][i]
        for i in range(1, len(A)):
            for j in range(2, min(K + 1, i + 1 + 1)):
                for k in range(max(i - 1, j - 1 - 1), -1, -1):
                    temp_last_group = means[k + 1][i]
                    temp_sum_prev = dp[k][j - 1]
                    dp[i][j] = max(dp[i][j], temp_last_group + temp_sum_prev)
        return dp[-1][-1]
