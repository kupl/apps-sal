class Solution:

    def knightDialer(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        dp = [[0 for _ in range(n + 1)] for _ in range(10)]
        for i in range(10):
            dp[i][1] = 1
        for j in range(2, n + 1):
            for i in range(10):
                for move in moves[i]:
                    dp[i][j] += dp[move][j - 1]
                    dp[i][j] %= MOD
        sum_ = 0
        for i in range(10):
            sum_ += dp[i][n]
            sum_ %= MOD
        return sum_
