class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        if len(A) < 2:
            return len(A)

        dp = [{} for i in range(len(A))]
        m = 2

        for i in range(1, len(A)):
            for j in range(0, i):

                diff = A[i] - A[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                    m = max(m, dp[i][diff])

                else:
                    if diff not in dp[i]:
                        dp[i][diff] = 2

        return m
