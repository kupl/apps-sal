class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        def findMax(l, h):
            return max(arr[l:h+1])
        for l in range(1,n):
            for i in range(n-l):
                j = i+l
                for k in range(i, j):
                    tmp = dp[i][k] + dp[k+1][j] + findMax(i,k)* findMax(k+1, j)
                    dp[i][j] = tmp if dp[i][j]==0 else min(dp[i][j], tmp)
                    
        return dp[0][-1]
                    

