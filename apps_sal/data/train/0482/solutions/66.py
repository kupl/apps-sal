class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        dp = [[float('inf') for i in range(len(arr))] for _ in range(len(arr))]
        
        for i in range(0, len(arr)):
            dp[i][i] = 0
        
        for i in range(0, len(arr)-1):
            dp[i][i+1] = arr[i]*arr[i+1]
            
        for l in range(2, len(arr)+1):
            for i in range(0, len(arr)-l):
                j = i+l
                for k in range(i+1, j+1):
                    dp[i][j] = min(dp[i][j], max(arr[i:k])*max(arr[k:j+1]) + dp[i][k-1] + dp[k][j])
        
        return dp[0][-1]
