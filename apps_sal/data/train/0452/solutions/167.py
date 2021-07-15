class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty): return -1
        m = len(jobDifficulty)
        dp = [[float('inf') for _ in range(m)] for _ in range(d)]
        for i in range(0, d):
            if i == 0:
                val = jobDifficulty[0]
                for j in range(m - d + i + 1):
                    val = max(jobDifficulty[j], val)
                    dp[i][j] = val
            else:
                for j in range(i, m - d + i + 1):
                    val = jobDifficulty[j]
                    for k in range(j - 1, i - 2, -1):
                        val = max(jobDifficulty[k + 1], val)
                        dp[i][j] = min(dp[i][j], dp[i - 1][k] + val)
        # print(dp)
        return dp[-1][-1]

