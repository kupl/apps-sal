class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = dict()
        max_len = 0
        for i in range(len(A)):
            dp[i] = dict()
            for j in range(i):
                d = A[i] - A[j]
                if d in dp[j]:
                    dp[i][d] = max(dp[i][d], 1 + dp[j][d]) if d in dp[i] else 1 + dp[j][d]
                else:
                    dp[i][d] = 2
                max_len = max(max_len, dp[i][d])

        return max_len
