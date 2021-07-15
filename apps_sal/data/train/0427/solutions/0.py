class Solution:
    def countOrders(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        
        p = (n-1)*2+1
        
        dp = [0 for i in range(n+1)]
        dp[1] = 1
        M= 10**9+7
        for i in range(2,n+1):
            
            p = (i-1)*2+1
            
            dp[i] = (dp[i-1]%M * ((p*(p+1))//2)%M)%M
        
        return dp[n]

