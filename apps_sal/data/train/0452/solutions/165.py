class Solution:
    def minDifficulty(self, jd: List[int], d: int) -> int:
        n = len(jd)
        if n < d:
            return -1
        dp = [[0] * n for _ in range(d)]
        dp[0][0] = jd[0]
        for i in range(1, n):
            dp[0][i] = max(jd[i], dp[0][i - 1])
        for i in range(1, d):
            for j in range(i, n):
                dp[i][j] = float('inf')
                curMax = jd[j]
                for r in range(j, i - 1, -1):
                    curMax = max(curMax, jd[r])
                    dp[i][j] = min(dp[i][j], dp[i - 1][r - 1] + curMax)

        return dp[d - 1][n - 1]
