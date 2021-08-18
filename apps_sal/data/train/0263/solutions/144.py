class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7

        dp = [[0 for _ in range(10)] for _ in range(n)]
        move = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [4, 2]]
        dp[0] = [1 for _ in range(10)]
        for i in range(1, n):
            for j in range(10):
                for nei in move[j]:
                    dp[i][j] = (dp[i][j] + dp[i - 1][nei]) % MOD
        return sum(dp[-1]) % MOD
