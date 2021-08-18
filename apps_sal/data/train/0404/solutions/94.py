import itertools


class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:

        dp = [[0] * len(A) for _ in range(K)]
        cur_sum = 0

        for j in range(len(A)):
            cur_sum += A[j]
            dp[0][j] = float(cur_sum) / (j + 1)

        for i in range(1, K):
            for j in range(len(A)):
                cur_sum = 0
                for k in range(j, i - 1, -1):
                    cur_sum += A[k]
                    dp[i][j] = max(dp[i][j], dp[i - 1][k - 1] + float(cur_sum) / (j - k + 1))

        return dp[-1][-1]
