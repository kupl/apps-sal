from functools import lru_cache
from bisect import bisect_left


class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)

        @lru_cache(None)
        def fib(p1, p2, i):
            prevsum = p1 + p2
            i = bisect_left(A, prevsum)
            if i < n and A[i] == prevsum:
                return 1 + fib(p2, A[i], i + 1)
            return 0
        res = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                curres = fib(A[i], A[j], j + 1)
                if curres:
                    res = max(res, 2 + curres)
        return res
