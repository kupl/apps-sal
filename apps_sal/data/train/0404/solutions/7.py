class Solution(object):
    def largestSumOfAverages(self, A, K):
        prefix_sum = [0]
        for x in A:
            prefix_sum.append(prefix_sum[-1] + x)

        def average(i, j):
            return (prefix_sum[j] - prefix_sum[i]) / (j - i)

        n = len(A)
        dp = [[0] * n for _ in range(K)]

        for k in range(K):
            for i in range(n):
                if k == 0 and i == 0:
                    dp[0][i] = A[0]
                elif k == 0:
                    dp[0][i] = average(0, i+1)
                else:
                    for j in range(i):
                        dp[k][i] = max(dp[k][i], dp[k - 1][j] + average(i+1, j+1))

        return dp[-1][-1]
