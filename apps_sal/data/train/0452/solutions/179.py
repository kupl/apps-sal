import functools
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n, inf = len(jobDifficulty), float('inf')
        if n < d:
            return -1
        dp = [inf]* n + [0]
        for day in range(1, d + 1):
            for i in range(n - day + 1):
                maxd, dp[i] = 0, inf
                for j in range(i, n - day + 1):
                    maxd = max(maxd, jobDifficulty[j])
                    dp[i] = min(dp[i], maxd + dp[j+1])
        return dp[0]
