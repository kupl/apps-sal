class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        from collections import defaultdict
        dp = [Counter() for _ in range(len(A))]
        max_length = 0
        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2
                max_length = max(max_length, dp[i][diff])
        return max_length
