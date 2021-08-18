class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        La = len(A)
        Lb = len(B)
        dp = [[0] * Lb for i in range(La)]

        for i in range(La):
            for j in range(Lb):
                if i == 0:
                    if A[i] == B[j]:
                        dp[i][j] = 1
                    elif j != 0:
                        dp[i][j] = dp[i][j - 1]
                else:
                    if j == 0:
                        if A[i] == B[j]:
                            dp[i][j] = 1
                        else:
                            dp[i][j] = dp[i - 1][j]
                    else:

                        if A[i] == B[j]:
                            dp[i][j] = dp[i - 1][j - 1] + 1
                        else:
                            dp[i][j] = dp[i - 1][j]
                        dp[i][j] = max(dp[i][j], dp[i][j - 1])
        return dp[-1][-1]
