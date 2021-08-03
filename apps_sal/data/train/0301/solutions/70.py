class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        M, N = len(A), len(B)
        dp = [0] * (N + 1)
        for i in range(M):
            for j in range(N)[::-1]:
                if B[j] == A[i]:
                    dp[j + 1] = dp[j] + 1
            for j in range(N):
                dp[j + 1] = max(dp[j + 1], dp[j])
        return dp[-1]
