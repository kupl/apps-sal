class Solution:

    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        maxi = 0
        n = len(A)
        dp = {}
        dp[0, L] = sum(A[0:L]) + sum(A[L:L + M])
        dp[M, 0] = sum(A[0:M]) + sum(A[M:L + M])
        for i in range(n - L + 1):
            for j in range(n - M + 1):
                if i >= j and i - j < M or (i < j and j - i < L):
                    continue
                else:
                    if (i, j - 1) in dp:
                        dp[i, j] = dp[i, j - 1] - A[j - 1] + A[j + M - 1]
                    elif (i - 1, j) in dp:
                        dp[i, j] = dp[i - 1, j] - A[i - 1] + A[i + L - 1]
                    maxi = max(maxi, dp[i, j])
        return maxi
