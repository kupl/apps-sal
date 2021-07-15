
class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],
                     [1,7,0],[2,6],[1,3],[2,4]]
        
        dp = [[0]*10  for _ in range(n)]
        for i in range(n):
            for j in range(10):
                dp[i][j] = 0
                
        for i in range(10):
            dp[0][i] = 1
            
        for t in range(1, n):
            for num in range(10):
                for move in moves[num]:
                    dp[t][num] += dp[t - 1][move]
                    dp[t][num] %= MOD
        return sum(dp[n-1])%MOD

