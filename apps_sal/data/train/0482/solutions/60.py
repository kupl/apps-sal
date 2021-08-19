class Solution:

    def mctFromLeafValues(self, arr: List[int]) -> int:
        dp = [[float('inf') for i in range(len(arr))] for j in range(len(arr))]
        for i in range(0, len(arr)):
            dp[i][i] = 0
        for l in range(2, len(arr) + 1):
            for i in range(0, len(arr) - l + 1):
                j = i + l - 1
                for k in range(i, j):
                    ans = max(max(arr[i:k + 1]), 0) * max(max(arr[k + 1:j + 1]), 0) + dp[i][k] + dp[k + 1][j]
                    dp[i][j] = min(dp[i][j], ans)
        return dp[0][len(arr) - 1]
