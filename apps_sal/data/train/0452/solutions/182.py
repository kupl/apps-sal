class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1

        # dp[i][j]表示第i天以第j个任务结尾，总的最小的difficulty
        dp = [[float('inf')] * len(jobDifficulty) for _ in range(d)]

        dp[0][0] = jobDifficulty[0]
        for j in range(1, len(jobDifficulty)):
            dp[0][j] = max(dp[0][j - 1], jobDifficulty[j])

        for i in range(1, d):
            for j in range(i, len(jobDifficulty)):
                maxdif = 0
                for k in range(j - 1, -1, -1):
                    maxdif = max(maxdif, jobDifficulty[k + 1])
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + maxdif)

        return dp[-1][-1]
