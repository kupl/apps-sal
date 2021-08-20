class Solution:

    def mctFromLeafValues(self, arr: List[int]) -> int:
        dp = [[0] * len(arr) for i in range(len(arr))]
        for i in range(len(arr) - 1, -1, -1):
            for j in range(i + 1, len(arr)):
                if j - i == 1:
                    dp[i][j] = arr[i] * arr[j]
                    continue
                m = 2 ** 32
                for k in range(i + 1, j + 1):
                    s = max(arr[i:k]) * max(arr[k:j + 1]) + dp[i][k - 1] + dp[k][j]
                    if s < m:
                        m = s
                dp[i][j] = m
        return dp[0][-1]
