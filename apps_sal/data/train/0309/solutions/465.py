class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        if len(A) == 0:
            return 0
        if len(A) == 1:
            return 1
        for i in range(1, len(A)):
            for j in range(0, i):
                diff = A[i] - A[j]

                if (j, diff) in dp:
                    dp[(i, diff)] = 1 + dp[(j, diff)]
                else:
                    dp[i, diff] = 2
        return max(dp.values())
