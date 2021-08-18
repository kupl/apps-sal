class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:

        dp: List[List[int]] = [[0 for i in range(len(B) + 1)] for j in range(len(A) + 1)]
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                if B[j - 1] == A[i - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
        return dp[len(A)][len(B)]
