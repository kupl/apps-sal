class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        n = len(A[0])
        dp = [1] * n
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if all(A[k][i] <= A[k][j] for k in range(len(A))):
                    dp[i] = max(dp[i], 1 + dp[j])
        return n - max(dp)
