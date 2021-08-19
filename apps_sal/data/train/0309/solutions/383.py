class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        m = 0
        for i in range(len(A)):
            for j in range(i):
                d = A[i] - A[j]
                j1 = (j, d)
                i1 = (i, d)
                if dp.get(j1) != None:
                    dp[i1] = 1 + dp[j1]
                else:
                    dp[i1] = 1
                m = max(m, dp[i1])
        return m + 1
