class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # dp = {}
        # n = len(A)
        # for i in range(1, n):
        #     for j in range(i):
        #         d = A[i] - A[j]
        #         if (j, d) in dp:
        #             dp[i, d] = dp[j, d] + 1
        #         else:
        #             dp[i, d] = 2
        # return max(dp.values())
        d = [collections.defaultdict(int) for _ in A]
        res = 1
        n = len(A)
        for i in range(n):
            for j in range(i):
                v = A[i]-A[j]
                d[i][v]=max(d[j][v]+1,d[i][v])
                res = max(d[i][v],res)
        return res+1
