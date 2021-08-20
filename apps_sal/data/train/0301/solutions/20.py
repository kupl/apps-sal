class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        (m, n) = (len(A), len(B))
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                left = dp[i][j - 1]
                up = dp[i - 1][j]
                leftup = dp[i - 1][j - 1]
                dp[i][j] = max(left, up, leftup + int(A[i - 1] == B[j - 1]))
                print(left, up, leftup)
        return dp[m][n]
