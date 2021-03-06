class Solution:

    def longestArithSeqLength(self, A):
        dp = []
        (ans, n) = (2, len(A))
        for i in range(n):
            dp.append(dict())
            for j in range(i - 1, -1, -1):
                diff = A[i] - A[j]
                if diff not in dp[i]:
                    dp[i][diff] = 2
                if diff in dp[j]:
                    dp[i][diff] = max(dp[j][diff] + 1, dp[i][diff])
                ans = max(ans, dp[i][diff])
        return ans
