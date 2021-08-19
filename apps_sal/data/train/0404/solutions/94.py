import itertools


class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        # Dynamic Programming
        # Time  complexity: O(K x N^2)
        # Space complexity: O(N)
        # P = [0] + list(itertools.accumulate(A))
        # def average(i, j): return (P[j] - P[i]) / float(j - i)

        # N = len(A)
        # dp = [average(i, N) for i in range(N)]
        # for _ in range(K - 1):
        #     for i in range(N):
        #         for j in range(i + 1, N):
        #             dp[i] = max(dp[i], average(i, j) + dp[j])

        # return dp[0]

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
