from collections import Counter


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if len(A) <= 2:
            return len(A)
        dp = [Counter() for _ in range(len(A))]
        ans = 2
        for i in range(len(A)):
            for j in range(i + 1, len(A), 1):
                diff = A[j] - A[i]
                if dp[i][diff] != 0:
                    dp[j][diff] = dp[i][diff] + 1
                else:
                    dp[j][diff] = 2
                ans = max(ans, dp[j][diff])
        return ans
