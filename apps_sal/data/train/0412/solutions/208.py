class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for _ in range(target + 1)] for _ in range(d + 1)]
        dp[0][0] = 1
        mod = 10 ** 9 + 7
        for i in range(1, d + 1):
            for j in range(1, target + 1):
                ff = 1
                highest_die = min(j, f)
                while ff <= highest_die:
                    dp[i][j] += dp[i - 1][j - ff]
                    dp[i][j] %= mod
                    ff += 1
        return dp[d][target] % mod
