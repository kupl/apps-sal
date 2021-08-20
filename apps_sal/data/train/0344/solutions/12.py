class Solution:

    def minDeletionSize(self, A):
        (m, n) = (len(A), len(A[0]))
        dp = [1] * n
        for j in range(1, n):
            for k in range(j):
                if all((A[i][k] <= A[i][j] for i in range(m))):
                    dp[j] = max(dp[j], dp[k] + 1)
        return n - max(dp)
