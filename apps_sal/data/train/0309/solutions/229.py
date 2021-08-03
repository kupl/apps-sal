class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        longest = 2
        dp = [{} for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                diff = A[i] - A[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2

                longest = max(longest, dp[i][diff])

        return longest
