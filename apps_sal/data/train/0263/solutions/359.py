class Solution:
    def knightDialer(self, n: int) -> int:
        moves = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]
        mod = 10**9 + 7
        dp = [[0 for j in range(10)] for i in range(n)]
        for i in range(10):
            dp[0][i] = 1
        for i in range(1, n):
            for j in range(10):
                for nei in moves[j]:
                    dp[i][nei] += dp[i - 1][j]
                    dp[i][nei] = dp[i][nei] % mod
        res = sum(dp[n - 1]) % mod
        return res
