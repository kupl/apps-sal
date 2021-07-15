class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if d > len(jobDifficulty): return -1
        m = len(jobDifficulty)
        dp = [float('inf') for _ in range(m)]
        dp[0] = jobDifficulty[0]
        for i in range(1, m): dp[i] = max(dp[i - 1], jobDifficulty[i])
        for i in range(1, d):
            for j in range(m - 1, i - 1, -1):
                dp[j] = float('inf')
                val = 0
                for k in range(j, i - 1, -1):
                    val = max(jobDifficulty[k], val)
                    dp[j] = min(dp[j], dp[k - 1] + val)
        # print(dp)
        return dp[-1]

