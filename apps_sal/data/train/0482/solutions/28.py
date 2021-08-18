class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:

        n = len(arr)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = 0
        for i in range(n - 1):
            dp[i][i + 1] = arr[i] * arr[i + 1]

        for l in range(2, n + 1):
            for i in range(n - l):
                j = i + l
                dp[i][j] = float('inf')
                for k in range(i + 1, j + 1):
                    q = dp[i][k - 1] + dp[k][j] + max(arr[i:k]) * max(arr[k: j + 1])
                    if q < dp[i][j]:
                        dp[i][j] = q

        return dp[0][-1]
