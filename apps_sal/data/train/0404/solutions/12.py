class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        cumsums = [0] * (len(A) + 1)
        for (i, x) in enumerate(A):
            cumsums[i + 1] = cumsums[i] + A[i]
        memo = {}

        def DP(j, K):
            if K == 0:
                return 0
            if j + 1 == K:
                return cumsums[j + 1]
            if K == 1:
                return cumsums[j + 1] / (j + 1)
            res = 0
            for i in range(j, -1, -1):
                if (i, K - 1) not in memo:
                    memo[i, K - 1] = DP(i, K - 1)
                if j - i == 0:
                    res = max(res, memo[i, K - 1])
                else:
                    res = max(res, memo[i, K - 1] + (cumsums[j + 1] - cumsums[i + 1]) / (j - i))
            return res
        a = DP(len(A) - 1, K)
        return a
