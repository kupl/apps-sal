class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # dp = {}
        # for i, a2 in enumerate(A[1:], start=1):
        #     for j, a1 in enumerate(A[:i]):
        #         print('a2: ' + str(a2) + '; a1: ' + str(a1))
        #         d = a2 - a1
        #         if (j, d) in dp:
        #             dp[i, d] = dp[j, d] + 1
        #         else:
        #             dp[i, d] = 2
        #         print(dp)
        # return max(dp.values())
        dp = {}
        for i, a2 in enumerate(A[1:], start=1):
            for j, a1 in enumerate(A[:i]):
                d = a2 - a1
                if (j, d) in dp:
                    dp[i, d] = dp[j, d] + 1
                else:
                    dp[i, d] = 2
        return max(dp.values())
