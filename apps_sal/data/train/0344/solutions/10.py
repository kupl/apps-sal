class Solution:
    def minDeletionSize(self, A: List[str]) -> int:

        m = len(A)
        n = len(A[0])
        dp = [1] * n
        res = n - 1
        for j in range(1, n):
            for i in range(j):
                k = 0
                while k < m and A[k][i] <= A[k][j]:
                    k += 1
                if k == m and (1 + dp[i]) > dp[j]:
                    dp[j] = 1 + dp[i]

            res = min(res, n - dp[j])
        return res
