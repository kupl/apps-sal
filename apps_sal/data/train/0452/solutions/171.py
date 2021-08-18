class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty):
            return -1

        dp = [[0] * (len(jobDifficulty)) for _ in range(d)]

        dp[0][0] = jobDifficulty[0]
        for i in range(1, len(jobDifficulty)):
            dp[0][i] = max(dp[0][i - 1], jobDifficulty[i])

        for di in range(1, d):
            for j in range(di, len(jobDifficulty)):
                localMax = jobDifficulty[j]
                dp[di][j] = 10 * 1000 + 1
                for r in range(j, di - 1, -1):
                    localMax = max(localMax, jobDifficulty[r])
                    dp[di][j] = min(dp[di][j], dp[di - 1][r - 1] + localMax)
        return dp[-1][-1]
