class Solution:
    def knightDialer(self, N: int) -> int:
        if N==0: return 0
        
        dp = [1]*10
        
        for i in range(N-1):
            temp = [0]*10
            temp[1], temp[2], temp[3] = dp[6]+dp[8], dp[7]+dp[9], dp[4]+dp[8]
            temp[4], temp[5], temp[6]  = dp[3]+dp[0]+dp[9], 0, dp[1]+dp[7]+dp[0]
            temp[7], temp[8], temp[9]  = dp[2]+dp[6], dp[1]+dp[3], dp[2]+dp[4]
            temp[0] = dp[4]+dp[6]
            dp = temp
            
        
        
        return sum(dp)%(10**9+7)

