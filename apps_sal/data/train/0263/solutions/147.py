class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7

        moves = [
            [4,6],[6,8],[7,9],[4,8],[3,9,0],[],
            [1,7,0],[2,6],[1,3],[2,4]
        ]
        
        dp = [[0] * 10 for _ in range(n + 1)]
        for i in range(10):
            dp[1][i] = 1
        
        for i in range(2, n + 1):
            for j in range(10):
                for move in moves[j]:
                    dp[i][move] += dp[i - 1][j]
                    dp[i][move] %= MOD
        
        return sum(dp[n]) % MOD
