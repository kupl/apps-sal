class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # 1 2 3
      # 6 6
      # 5 6 11 0 11 10 9
        # init
        # dp[j][d+1], if j < d, dp[j][d] = -1, dp[0][0] = 0
        # transition
        # 0 < k < d, dp[j][k] = min[dp[i][k-1] + max(i..j)]
        # answer dp[n][d]

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
