class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # dp
        # time: O(n^2 * d)
        # space: O(nd)

        # dp[i][j]=min(dp[k][j-1]+max(jobD[k:i]))

        if len(jobDifficulty) < d:
            return -1

        n = len(jobDifficulty)
        dp = [[float('inf')] * (d + 1) for _ in range(n + 1)]

        maxVal = {}

        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                maxVal[(i, j)] = max(jobDifficulty[i:j])

        for i in range(1, n + 1):
            dp[i][1] = max(jobDifficulty[:i])

        for i in range(1, n + 1):
            for j in range(2, d + 1):
                if i >= j:
                    for k in range(j - 1, i):
                        dp[i][j] = min(dp[i][j], dp[k][j - 1] + maxVal[(k, i)])

        return dp[n][d]
