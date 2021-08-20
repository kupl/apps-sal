class Solution:

    def longestCommonSubsequence(self, a: str, b: str) -> int:
        (m, n) = (len(a), len(b))
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if a[i] == b[j]:
                    dp[i][j] = 1 + (dp[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0)
                else:
                    dp[i][j] = max(dp[i][j - 1] if j - 1 >= 0 else 0, dp[i - 1][j] if i - 1 >= 0 else 0)
        print(dp)
        return dp[-1][-1]
