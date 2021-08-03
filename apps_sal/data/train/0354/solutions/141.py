import functools


class Solution:
    def dieSimulator(self, n: int, R: List[int]) -> int:
        @functools.lru_cache(None)
        def g(n, k):
            if n < 1:
                return 0
            if n == 1:
                return 1
            return f(n - 1) - f(n - R[k - 1] - 1) + g(n - R[k - 1] - 1, k)

        @functools.lru_cache(None)
        def f(n):
            if n < 0:
                return 0
            if n == 0:
                return 1
            return sum([g(n, k) for k in range(1, 7)])

        return f(n) % (10 ** 9 + 7)
