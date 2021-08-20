class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        jD = jobDifficulty
        N = len(jD)
        if d > N:
            return -1
        dp = [[float('inf')] * N for _ in range(d)]
        dp[0][0] = jD[0]
        for j in range(1, N):
            dp[0][j] = 0
            dp[0][j] = max(dp[0][j - 1], jD[j])
        for i in range(1, d):
            for j in range(i, N):
                last_dayD = jD[j]
                for k in range(j - 1, i - 2, -1):
                    last_dayD = max(last_dayD, jD[k + 1])
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + last_dayD)
        return dp[d - 1][N - 1]
