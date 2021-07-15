class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        dp = [[sys.maxsize] * len(arr) for i in range(len(arr))]
        for i in range(0, len(arr)):
            dp[i][i] = 0
        
        for length in range(2, len(arr)+1):
            for i in range(0, len(arr)-length+1):
                j = i+length-1
                for k in range(i, j):
                    temp = max(arr[i:k+1])*max(arr[k+1:j+1])+dp[i][k]+dp[k+1][j]
                    dp[i][j] = min(dp[i][j], temp)
        
        return dp[0][-1]

