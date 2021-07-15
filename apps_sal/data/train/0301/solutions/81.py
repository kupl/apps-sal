class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
        last_a = {}
        last_b = {}
        for i in range(len(A)):
            last_a[A[i]] = i
            for j in range(len(B)):
                last_b[B[j]] = j
                if A[i] == B[j]:
                    dp[i + 1][j + 1] = max(dp[i][j] + 1, dp[i + 1][j], dp[i][j + 1])
                else:
                    dp[i + 1][j + 1] = max(dp[i][j], dp[i + 1][last_b.get(A[i], -1) + 1], dp[last_a.get(B[j], -1) + 1][j + 1])
        return dp[-1][-1]
