class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        (l, w) = (len(A), len(B))
        dp = [[0] * (w + 1) for _ in range(l + 1)]
        for i in range(l):
            for x in range(w):
                if A[i] == B[x]:
                    dp[i + 1][x + 1] = dp[i][x] + 1
                else:
                    dp[i + 1][x + 1] = max(dp[i + 1][x], dp[i][x + 1])
        return dp[-1][-1]
