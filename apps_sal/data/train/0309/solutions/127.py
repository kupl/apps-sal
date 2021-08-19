class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}

        for i in range(len(A)):
            samecnt = 1
            for j in range(i):
                diff = A[i] - A[j]
                if diff == 0:
                    samecnt += 1
                else:
                    dp[A[i], diff] = dp.get((A[j], diff), 1) + 1
            dp[A[i], 0] = samecnt

        # print(dp)
        key = max(dp, key=dp.get)
        return dp[key]
