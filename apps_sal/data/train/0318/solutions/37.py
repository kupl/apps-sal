class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n=len(slices)
        dp=[[0 for j in range(n//3)] for i in range(n)]
        
        dp[0][0]=slices[0]
        
        for i in range(1,n):
            dp[i][0]=max(dp[i-1][0],slices[i])
        
        for i in range(2,n):
            for j in range(1,min(i//2+1,n//3)):
                dp[i][j]=max(dp[i-1][j],dp[i-2][j-1]+slices[i])
        
        mx=0
        
        for i in range(n-1):
            mx=max(mx,dp[i][-1])
            
        for i in range(n):
            for j in range(n//3):
                dp[i][j]=0
        
        for i in range(1,n):
            dp[i][0]=max(dp[i-1][0],slices[i])
        
        for i in range(2,n):
            for j in range(1,min(i//2+1,n//3)):
                dp[i][j]=max(dp[i-1][j],dp[i-2][j-1]+slices[i])
        
        mx=max(mx,dp[-1][-1])
        return mx
