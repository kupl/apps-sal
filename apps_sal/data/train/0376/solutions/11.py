class Solution:
    def minScoreTriangulation(self, a: List[int]) -> int:
        n = len(a)
        dp = [[(float('inf') if i-j>2 else 0)  for i in range(len(a))]for j in range(len(a)) ]
        for i in range(2, len(dp)):
            dp[i-2][i]=a[i-2]*a[i-1]*a[i]

        for l in range(3, len(dp)):
            for i in range(0, n-l):
                j= l+i
                if j>n:
                    break
                for k in range(i+1,j):
                    dp[i][j]=min(dp[i][j], a[k]*a[i]*a[j] + dp[i][k]+dp[k][j])
                    
        return dp[0][-1]
                    
                

