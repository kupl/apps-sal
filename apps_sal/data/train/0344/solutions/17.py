class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        n, m = len(A[0]), len(A)
        dp = [1] * n
        for j in range(1, n):
            for i in range(j):
                if all(A[k][i] <= A[k][j] for k in range(m)):
                    dp[j] = max(dp[j], 1 + dp[i])
        return n - max(dp)
