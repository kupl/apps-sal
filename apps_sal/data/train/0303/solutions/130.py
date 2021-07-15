class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        
        
        dp=[0 for _ in A]
        
        for i,num in enumerate(A):
            for j in range(K):
                ans=0            
                if i-j>=0:
                    ans = ans + (j+1)*max(A[i-j:i+1])
                if i-j-1>=0:
                    ans = ans + dp[i-j-1]
                dp[i]=max(dp[i],ans)
                
                
#                 if i-p-1>=0:
#                     ans=dp[i-p-1]+(p+1)*max(A[i-p:i+1])
#                     print(A[i-p-1],(p+1)*max(A[i-p:i+1]))
#                     dp[i]=max(dp[i],ans)
        
        #print(dp)
        
        return dp[-1]

