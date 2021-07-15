#O(N*K)
#O(1)

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        
        #find max no of floor you can reach with given eggs and no of attempts
        
        dp = [ [0 for j in range(K+1)] for i in range(N+1)]
        
        attempt = 0
        while(dp[attempt][K]<N):
            attempt+=1
            for j in range(1,len(dp[0])):
                # 1 + Break case + No Break case
                dp[attempt][j]= 1 + dp[attempt-1][j-1]+ dp[attempt-1][j]
                if dp[attempt][j]>=N:
                    return attempt
        
                

