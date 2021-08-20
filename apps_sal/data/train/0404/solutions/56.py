class Solution:

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        accsum = A[:]
        l = len(accsum)
        for i in range(1, l):
            accsum[i] += accsum[i - 1]
        cache = {}

        def dp(i, k):
            prev = accsum[i - 1] if i > 0 else 0
            if k == 1:
                res = (accsum[l - 1] - prev) / (l - i)
                cache[i, k] = res
                return res
            if (i, k) in cache:
                return cache[i, k]
            if l - i < k:
                return -float('inf')
            if l - i == k:
                res = accsum[l - 1] - prev
                cache[i, k] = res
                return res
            res = 0
            for j in range(i, l - k + 1):
                res = max(res, (accsum[j] - prev) / (j - i + 1) + dp(j + 1, k - 1))
            cache[i, k] = res
            return res
        return dp(0, K)
