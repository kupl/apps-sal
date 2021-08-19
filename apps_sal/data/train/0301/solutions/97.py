class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        max_val = 0
        (m, n) = (len(A), len(B))
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i - 1][j], dp[i][j - 1])
                else:
                    dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
                max_val = max(max_val, dp[i][j])
        return max_val
