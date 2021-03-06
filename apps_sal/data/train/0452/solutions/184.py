class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        M = 1000000.0
        dp = [M for i in range(n + 1)]
        dp[n] = 0
        for j in range(1, d + 1):
            for i in range(n):
                m = -1
                dp[i] = M
                for k in range(i, n):
                    m = max(m, jobDifficulty[k])
                    dp[i] = min(dp[i], m + dp[k + 1])
            dp[n] = M
        return dp[0] if dp[0] < M else -1
