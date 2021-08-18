class Solution:

    def qute_print(self, A):
        for row in A:
            for elem in row:
                print('{:2}'.format(elem), end=' ')
            print()

    def isInterleave(self, A, B, C):
        n, m = len(A), len(B)

        if len(C) != n + m:
            return False

        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, n + 1):
            dp[i][0] = bool(dp[i - 1][0] * (A[i - 1] == C[i - 1]))

        for j in range(1, m + 1):
            dp[0][j] = bool(dp[0][j - 1] * (B[j - 1] == C[j - 1]))

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] == C[i + j - 1]:
                    dp[i][j] = dp[i - 1][j]
                if not dp[i][j] and B[j - 1] == C[i + j - 1]:
                    dp[i][j] = dp[i][j - 1]

        return dp[-1][-1]
