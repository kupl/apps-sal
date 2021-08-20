class Solution:

    def mctFromLeafValues(self, arr: List[int]) -> int:
        n = len(arr)
        max_dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            temp = arr[i]
            for j in range(i, n):
                temp = max(temp, arr[j])
                max_dp[i][j] = temp
        dp = [[-1 for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = 0
        for i in range(n - 1):
            dp[i][i + 1] = arr[i] * arr[i + 1]
        for k in range(2, n):
            for i in range(n):
                j = i + k
                if j >= n:
                    break
                dp[i][j] = dp[i][i] + dp[i + 1][j] + arr[i] * max_dp[i + 1][j]
                for s in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][s] + dp[s + 1][j] + max_dp[i][s] * max_dp[s + 1][j])
        return dp[0][-1]
