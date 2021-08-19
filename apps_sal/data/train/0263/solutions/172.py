class Solution:
    def knightDialer(self, n: int) -> int:
        moves = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}

        # dp[i][j] = x
        # x possible calls of length i when knight is placed on j

        dp = [[0 for j in range(10)] for i in range(n)]

        for i in range(n):
            for j in range(10):
                if i == 0:
                    dp[i][j] = 1
                else:
                    for move in moves[j]:
                        dp[i][j] += dp[i - 1][move]

        return sum(dp[n - 1]) % (10 ** 9 + 7)
