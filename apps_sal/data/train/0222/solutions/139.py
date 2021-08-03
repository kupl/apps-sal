from functools import lru_cache


class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        S = set(A)

        @lru_cache(None)
        def fib(p1, p2):
            prevsum = p1 + p2
            if prevsum in S:
                return 1 + fib(p2, prevsum)
            return 0

        res = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                curres = fib(A[i], A[j])
                if curres:
                    res = max(res, 2 + curres)
        return res
