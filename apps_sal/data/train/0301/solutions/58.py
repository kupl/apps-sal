class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        if not A or not B:
            return 0
        dp = [[0 for _ in range(len(A) + 1)] for _ in range(len(B) + 1)]
        for i in range(len(B) + 1):
            for j in range(len(A) + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif B[i - 1] == A[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[-1][-1]
