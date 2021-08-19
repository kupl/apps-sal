class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        (na, nb) = (len(A), len(B))
        dp = [[0 for i in range(nb + 1)] for j in range(na + 1)]
        for i in range(na):
            for j in range(nb):
                if A[i] == B[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i + 1][j], dp[i][j + 1])
        return dp[-1][-1]
