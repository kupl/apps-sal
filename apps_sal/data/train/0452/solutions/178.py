class Solution:
    def minDifficulty(self, arr: List[int], d: int) -> int:
        n = len(arr)
        if d==1: return max(arr)
        if d>n: return -1
        if d==n: return sum(arr)
        dp = [[float('inf') for _ in range(n)] for _ in range(d)]
        #initialization
        dp[0][0] = arr[0]
        for i in range(1,n):
            dp[0][i] = max(dp[0][i-1], arr[i])
        for i in range(1,d):
            for j in range(i, n):
                diff = 0
                for k in range(j, i-1, -1):
                    diff = max(arr[k], diff)
                    dp[i][j] = min(dp[i][j], dp[i-1][k-1] + diff)
        return dp[d-1][n-1]
