class Solution:
    def knightDialer(self, N: int) -> int:
        moves = [[4,6],[6,8],[7,9],[4,8],[3,9,0],[],
                 [1,7,0],[2,6],[1,3],[2,4]]
        
        
        # dp[i] denotes the number of combinations starting from i
        dp = [1] * 10
        
        for n in range(N-1):
            newdp = [0] * 10
            for i in range(10):
                for j in moves[i]:
                    newdp[i] += dp[j] 
                    newdp[i] %= (10**9 + 7)
            dp = newdp
            
        return sum(dp) % (10**9 + 7)

