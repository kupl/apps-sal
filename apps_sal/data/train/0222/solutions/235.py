class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:

        # # straight forward N^2log(N)
        # n = len(A)
        # s = set()
        # for i in A:
        #     s.add(i)
        # res = 0
        # ll = 0
        # for i in range(n):
        #     for j in range(i+1,n):
        #         f1 = A[i]
        #         f2 = A[j]
        #         if f1+f2 in s:
        #             ll = 2
        #         while f1+f2 in s:
        #             ll += 1
        #             tmp = f2
        #             f2 = f1+f2
        #             f1 = tmp
        #         res = max(res,ll)
        # return res

        # DP N^2 time N^2 space
        n = len(A)
        d = {}
        for i in range(n):
            d[A[i]] = i
        dp = [[0] * n for i in range(n)]
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                tar = A[i] + A[j]
                if tar in d:
                    k = d[tar]
                    dp[j][k] = max(dp[j][k], dp[i][j] + 1, 3)
            res = max(res, max(dp[i]))
            # print(res,i,j,dp)
        return res
