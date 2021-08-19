class Solution:

    def minDeletionSize(self, A: List[str]) -> int:
        m = len(A)
        n = len(A[0])
        dp = [1 for i in range(n)]
        maxVal = 1

        def check(i, j):
            for k in range(m):
                if A[k][i] < A[k][j]:
                    return False
            return True
        for i in range(1, n):
            for j in range(i):
                if check(i, j):
                    dp[i] = max(dp[i], dp[j] + 1)
            maxVal = max(maxVal, dp[i])
        return n - maxVal
