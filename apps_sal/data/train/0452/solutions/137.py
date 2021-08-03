import sys


class Solution:
    def minDifficulty(self, complexity: List[int], days: int) -> int:
        if not complexity:
            return 0
        if len(complexity) < days:
            return -1
        m = days
        n = len(complexity)
        dp = [[sys.maxsize] * (n) for _ in range(m)]

        cur_max = complexity[0]
        for j in range(n):
            cur_max = max(complexity[j], cur_max)
            dp[0][j] = cur_max

        for i in range(1, m):
            for j in range(0, n):
                for k in range(0, j):
                    cur_max = max(complexity[k + 1: j + 1])
                    dp[i][j] = min(dp[i][j], dp[i - 1][k] + cur_max)

        # print(dp)
        return dp[-1][-1]
