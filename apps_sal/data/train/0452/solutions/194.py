class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        dp = [[math.inf for _ in range(d + 1)] for _ in range(n + 1)]
        dp[0][0] = 0
        for j in range(0, n + 1):
            for k in range(1, d + 1):
                dp[j][k] = math.inf
                mx = 0
                for i in reversed(range(j)):
                    mx = max(mx, jobDifficulty[i])
                    dp[j][k] = min(dp[j][k], dp[i][k - 1] + mx)
        print(dp)
        return dp[n][d]
