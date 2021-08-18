class Solution:
    def numWays(self, steps: int, arrlen: int) -> int:
        mod = 10 ** 9 + 7
        if arrlen == 1:
            return 1
        dp = [[0] * min(arrlen, steps + 1) for _ in range(steps + 1)]
        dp[1][0] = 1
        dp[1][1] = 1
        for a in range(2, steps + 1):
            dp[a][0] = (dp[a - 1][0] + dp[a - 1][1]) % mod
            for b in range(1, min(arrlen, a + 1)):
                if b == arrlen - 1 or b == a:
                    dp[a][b] = (dp[a - 1][b] + dp[a - 1][b - 1]) % mod
                else:
                    dp[a][b] = (dp[a - 1][b] + dp[a - 1][b + 1] + dp[a - 1][b - 1]) % mod
        return dp[-1][0]
