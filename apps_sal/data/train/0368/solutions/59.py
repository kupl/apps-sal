class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        sat=sorted(satisfaction)
        # print(sat)
#         self.ans=0
        
#         def traverse(ind,sat,time,gain):
#             if(ind==len(sat)):
#                 self.ans=max(self.ans,gain)
#                 return 
#             traverse(ind+1,sat,time,gain)
#             traverse(ind+1,sat,time+1,gain+time*sat[ind])
        
#         traverse(0,sat,1,0)
        
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
#         for i in dp:
#             print(i)
                
                
                
    
        return ans
