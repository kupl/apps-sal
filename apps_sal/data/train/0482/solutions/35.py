class Solution:

    def mctFromLeafValues(self, arr: List[int]) -> int:
        N = len(arr)
        dp = [[float('inf')] * N for _ in range(N)]
        for i in range(N - 1, -1, -1):
            for j in range(i, N):
                if i == j:
                    dp[i][j] = 0
                    continue
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + max(arr[i:k + 1]) * max(arr[k + 1:j + 1]))
        return dp[0][N - 1]
