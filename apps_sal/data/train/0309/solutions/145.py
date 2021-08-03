class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if len(A) <= 2:
            return len(A)
        n, ans = len(A), 0
        dp = [[0] * 1001
              for _ in range(n)]
        for j in range(n):
            for i in range(0, j):
                diff = A[j] - A[i] + 500
                dp[j][diff] = dp[i][diff] + 1
                ans = max(ans, dp[j][diff])

        return ans + 1
