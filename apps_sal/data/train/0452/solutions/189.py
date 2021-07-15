import sys

class Solution:
    def minDifficulty(self, complexity: List[int], days: int) -> int:
        n = len(complexity)
        if n < days:
            return -1
        dp = [[sys.maxsize] * (days + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n+1):
            for j in range(1, days+1):
                cur_max = 0
                for k in range(i - 1, j - 2, -1):
                    cur_max = max(cur_max, complexity[k])
                    dp[i][j] = min(dp[i][j], dp[k][j-1] + cur_max)
        return dp[-1][-1]

