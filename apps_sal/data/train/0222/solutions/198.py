class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:

        n = len(A)
        d = {}
        for i in range(n):
            d[A[i]] = i
        dp = {}
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                tar = A[i] + A[j]
                if tar in d:
                    k = d[tar]
                    dp[(j, k)] = max(dp.get((i, j), 2) + 1, dp.get((j, k), 2))
                    res = max(res, dp[(j, k)])
        return res
