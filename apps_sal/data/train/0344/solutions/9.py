class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        m = len(A[0])
        n = len(A)
        dp = [1] * m
        for i in range(1, m):
            for j in range(i):
                if all(a[j] <= a[i] for a in A):
                    dp[i] = max(dp[i], dp[j] + 1)
        return m - max(dp)
