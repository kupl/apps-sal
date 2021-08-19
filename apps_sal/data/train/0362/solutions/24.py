class Solution:

    def numberWays(self, hats: List[List[int]]) -> int:
        MOD = int(1000000000.0) + 7
        n = len(hats)
        dp = [[0 for _ in range(1 << n)] for _ in range(41)]
        rev = [[] for _ in range(41)]
        for (i, h) in enumerate(hats):
            for e in h:
                rev[e].append(i)
        dp[0][0] = 1
        for i in range(40):
            r = rev[i + 1]
            for j in range(1 << n):
                dp[i + 1][j] += dp[i][j]
                dp[i + 1][j] %= MOD
                for k in r:
                    if not j & 1 << k:
                        dp[i + 1][j | 1 << k] += dp[i][j]
                        dp[i + 1][j | 1 << k] %= MOD
        return dp[40][(1 << n) - 1]
