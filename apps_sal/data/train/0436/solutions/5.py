class Solution:
    def minDays(self, n: int) -> int:
        
        dp = [0]*(1000)
        
        
        for i in range(1,1000):
            dp[i] = dp[i-1]+1
            if i % 2 == 0:
                dp[i] = min(dp[i//2]+1, dp[i])
            if i % 3 == 0:
                dp[i] = min(dp[i//3]+1, dp[i])
        #print(dp)
        
        #for i in range(25,35):
        #    print(i, dp[i])
        
        
        d ={}
        d[0] = 0
        d[1] = 1
        
        def cal(k):
            if k in d:
                return d[k]
            
            a = k
            a = min(a, cal(k // 3) + k % 3+1)
            a = min(a, cal(k // 2) + k % 2+1)
            d[k] = a
            return d[k]
        
        for i in range(1,999):
            if(dp[i]!=cal(i)):
                print((i,dp[i],cal(i)))
        
        return cal(n)
        
        

