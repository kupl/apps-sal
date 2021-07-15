class Solution:
    def maxUncrossedLines(self, A, B):
        # Optimization
        commons = set(A).intersection(set(B)) # or commons = set(A) & set(B)
        A = [x for x in A if x in commons]
        B = [x for x in B if x in commons]

        N, M = len(A), len(B)
        dp = [[0] * (M + 1) for _ in range(N + 1)]
        for i in range(N):
            for j in range(M):
                if A[i] == B[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[-1][-1]
