class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10**9 + 7
        moves = [[4,6], [6,8], [7,9], [4,8], [0,3,9], [], [0,1,7], [2,6], [1,3], [2,4]]
        
        dp = [1]*10
        
        for i in range(n-1):
            new_dp = [0]*10
            
            for c, val in enumerate(dp):
                for j in moves[c]:
                    new_dp[j] += val
                    new_dp[j] %= mod
                    
                dp = new_dp
                
        return (sum(dp))%mod
        

