class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[0 for j in range(n)] for i in range(n)]
        for i in range(n - 2, -1, -1):
            dp[i][i + 1] = arr[i] * arr[i + 1]
            for j in range(i + 2, n):
                dp[i][j] = float('inf')
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + max(arr[i:k + 1]) * max(arr[k + 1:j + 1]))
        return dp[0][n - 1]
