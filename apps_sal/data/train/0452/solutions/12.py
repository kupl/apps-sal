class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty):
            return -1
        if not jobDifficulty:
            return 0
        dp = [[float('inf') for _ in range(d + 1)] for _ in range(len(jobDifficulty) + 1)]
        dp[0][0] = 0
        for i in range(1, len(jobDifficulty) + 1):
            for j in range(1, d + 1):
                tmp = 0
                for k in range(i, j - 1, -1):
                    tmp = max(tmp, jobDifficulty[k - 1])
                    dp[i][j] = min(dp[i][j], dp[k - 1][j - 1] + tmp)
        return dp[-1][-1] if dp[-1][-1] < float('inf') else -1
