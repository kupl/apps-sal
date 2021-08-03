class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        len_a = len(A) + 1
        len_b = len(B) + 1

        dp = [[0 for i in range(len_b)] for i in range(len_a)]

        for i in range(1, len_a):
            for j in range(1, len_b):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[len_a - 1][len_b - 1]
