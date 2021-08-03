class Solution:
    def minDeletionSize(self, A: List[str]) -> int:

        l = len(A[0])
        dp = [1 for _ in range(l)] + [0]
        for i in range(len(dp) - 1, -1, -1):
            for j in range(i + 1, l):
                if all(A[k][i] <= A[k][j] for k in range(len(A))):
                    dp[i] = max(dp[i], dp[j] + 1)

        return l - max(dp)
