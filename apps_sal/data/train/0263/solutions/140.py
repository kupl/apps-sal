class Solution:

    def knightDialer(self, n: int) -> int:
        nextMove = [(4, 6), (6, 8), (7, 9), (4, 8), (0, 3, 9), (), (0, 1, 7), (2, 6), (1, 3), (2, 4)]
        dp = [[0] * 10 for _ in range(n)]
        if n == 1:
            return 10
        MOD = 10 ** 9 + 7
        for i in range(10):
            dp[0][i] = 1
        for r in range(1, n):
            for i in range(10):
                for m in nextMove[i]:
                    dp[r][m] = dp[r][m] + dp[r - 1][i]
        return sum(dp[-1]) % MOD
