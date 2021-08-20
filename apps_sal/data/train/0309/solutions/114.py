class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = {}
        s = set(A)
        for i in range(1, n):
            for j in range(i):
                d = A[i] - A[j]
                if j != 0 and (j, d) in dp:
                    dp[i, d] = 1 + dp[j, d]
                else:
                    dp[i, d] = 2
        l = dp.values()
        return max(l)
