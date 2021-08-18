class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:

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
        return res
