class Solution:

    def knightDialer(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        dp = [[0] * 10 for _ in range(n)]
        for i in range(10):
            dp[0][i] = 1
        for i_n in range(0, n - 1):
            for i in range(10):
                for nei in moves[i]:
                    dp[i_n + 1][nei] += dp[i_n][i]
                    dp[i_n + 1][nei] %= MOD
        res = 0
        for i in range(10):
            res += dp[n - 1][i]
            res %= MOD
        return res
