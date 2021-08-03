class Solution(object):
    def largestSumOfAverages(self, A, K):
        p = [0]
        for x in A:
            p.append(x + p[-1])

        def avg(i, j):
            return (p[j] - p[i]) / (j - i)
        N = len(A)
        dp = [avg(i, N) for i in range(N)]
        for k in range(K - 1):
            for i in range(N):
                for j in range(i + 1, N):
                    dp[i] = max(dp[i], avg(i, j) + dp[j])
        return dp[0]
