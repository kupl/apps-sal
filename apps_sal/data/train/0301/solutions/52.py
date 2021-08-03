class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:

        rows = len(A)
        cols = len(B)
        dp = [[0 for i in range(cols + 1)] for j in range(rows + 1)]

        for i in range(rows):
            for j in range(cols):
                if A[i] == B[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], dp[i][j])

        return dp[rows][cols]
