class Solution:

    def mctFromLeafValues(self, arr: List[int]) -> int:
        dp = [[0 for i in range(len(arr))] for j in range(len(arr))]
        for i in range(len(arr)):
            dp[i][i] = (0, arr[i])
        for v in range(1, len(arr)):
            for j in range(v, len(arr)):
                i = j - v
                D_i_j = min((dp[i][k][0] + dp[k + 1][j][0] + dp[i][k][1] * dp[k + 1][j][1] for k in range(i, j)))
                M_i_j = max(dp[i][j - 1][1], arr[j])
                dp[i][j] = (D_i_j, M_i_j)
        return dp[0][len(arr) - 1][0]
