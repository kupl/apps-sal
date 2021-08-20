class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = []
        mod = math.pow(10, 9) + 7
        for _ in range(d + 1):
            dp.append((target + 1) * [0])
        for i in range(target + 1):
            dp[0][i] = 0
        for i in range(d + 1):
            dp[i][0] = 0
        for i in range(min(f, target)):
            dp[1][i + 1] = 1
        for i in range(2, d + 1):
            for j in range(1, target + 1):
                for roll in range(1, f + 1):
                    if j - roll >= 0:
                        dp[i][j] = (dp[i][j] % mod + dp[i - 1][j - roll] % mod) % mod
        return int(dp[d][target])
