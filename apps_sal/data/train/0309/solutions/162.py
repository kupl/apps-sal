class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = []
        for i in range(len(A)):
            dp.append({})

        res = 2
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2
                res = max(res, dp[i][diff])

        return res
