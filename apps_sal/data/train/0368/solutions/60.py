class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        sat=sorted(satisfaction)
        
        dp=[[-float('inf')]*(len(sat)+1) for i in range(len(sat)+1)]
        
        for i in range(len(sat)+1):
            dp[0][i]=0
        
        # for i in dp:
        #     print(i)
        
        ans=0
        
        for i in range(1,len(sat)+1): # time
            for j in range(i,len(sat)+1):  # items
                dp[i][j]=max(dp[i][j],dp[i-1][j-1]+sat[j-1]*i)
                ans=max(ans,dp[i][j])
            
                
#         print(\"after\")
        # for i in dp:
        #     print(i)
                
        return ans
