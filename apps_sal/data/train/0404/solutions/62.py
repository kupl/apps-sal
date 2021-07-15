class Solution:
    def largestSumOfAverages(self, a: List[int], k: int) -> float:
        def rec(st, k):
            if (st, k) in cache:
                return cache[(st, k)]
            if k == 1:
                cache[(st, k)] = sum(a[st:])/(len(a)-st)
                return cache[(st, k)]
            total = 0
            res = -math.inf
            for i in range(st, len(a)-k+1):
                total += a[i]
                res = max(res, (total/(i-st+1)) + rec(i+1, k-1))
            cache[(st, k)] = res
            return cache[(st, k)]
        cache = {}
        return rec(0, k)

