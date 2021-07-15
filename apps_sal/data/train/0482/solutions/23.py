class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        if not arr:
            return 0
        ans = 0
        n = len(arr)
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        maxi = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
            maxi[i][i] = arr[i]
            
        for l in range(1, n+1):
            for i in range(n-l+1):
                j = i + l - 1
                for k in range(i,j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + maxi[i][k] * maxi[k+1][j] + dp[k+1][j])
                for k in range(i,j+1):
                    maxi[i][j] = max(maxi[i][j], arr[k])
        return dp[0][-1]

