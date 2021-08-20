class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = [{} for i in range(len(A))]
        longest = 0
        for i in range(len(A)):
            for j in range(0, i):
                diff = A[i] - A[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2
                longest = max(longest, dp[i][diff])
        return longest
