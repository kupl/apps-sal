class Solution:
    def soupServings(self, N: int) -> float:
        n=N//25 + (N % 25 > 0)
        if n>=500:
            return 1
        dp=[[0]*(n+1) for i in range(n+1)]
        dp[-1][-1]=1
        
        x=[-4,-3,-2,-1]
        y=[0,-1,-2,-3]
        for i in range(n,0,-1):
            for j in range(n,0,-1):
                for dx,dy in zip(x,y):
                    if i+dx<0 and j+dy<0:
                        dp[0][0]+=dp[i][j]*(0.25)
                    elif i+dx<0:
                        dp[0][j+dy]+=dp[i][j]*(0.25)
                    elif j+dy<0:
                        dp[i+dx][0]+=dp[i][j]*(0.25)
                    else:
                        dp[i+dx][j+dy]+=dp[i][j]*(0.25)
                        
            
        Sum=0
        for j in range(n+1):
            Sum+=dp[0][j]
                
        return Sum - dp[0][0] / 2
            

# class Solution:
#     def soupServings(self, N: int) -> float:
#         N = N//25 + (N % 25 > 0)
#         if N >= 500:
#             return 1
#         dp = [[0]*(N+1) for _ in range(N+1)]
#         operations = [(4, 0), (3, 1), (2, 2), (1, 3)]
#         dp[-1][-1] = 1
        
#         for i in range(N, 0, -1):
#             for j in range(N, 0, -1):
#                 for a, b in operations:
#                     if i-a < 0 and j-b < 0:
#                         dp[0][0] += dp[i][j]*0.25
#                     elif i-a < 0:
#                         dp[0][j-b] += dp[i][j]*0.25
#                     elif j-b < 0:
#                         dp[i-a][0] += dp[i][j]*0.25
#                     else:
#                         dp[i-a][j-b] += dp[i][j]*0.25    
#         a_total = 0
#         for i in range(N+1):
#             a_total += dp[0][i]
        
#         return a_total - dp[0][0] / 2
            
            
                    
                
                

