class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        #         dp = {}
        #         res = -1
        #         for i in range(0, len(A)):
        #             for j in range(i-1, -1, -1):
        #                 d = A[i] - A[j]
        #                 dp[(i, d)] = max(dp.get((i, d), -1), dp.get((j, d), 1) + 1)
        #                 res = max(res, dp[(i, d)])

        #         return res
        dp = [[-1 for i in range(1001)] for j in range(len(A))]
        res = -1
        for i in range(0, len(A)):
            for j in range(i - 1, -1, -1):
                d = A[i] - A[j] + 500
                if dp[j][d] == -1:
                    dp[j][d] = 1
                dp[i][d] = max(dp[i][d], dp[j][d] + 1)
                res = max(res, dp[i][d])

        return res
