class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        def g(n, k):
            if n < 1:
                return 0
            if n == 1:
                return 1
            if (n, k) in g_cache:
                return g_cache[n, k]
            ans = f(n - 1) - f(n - rollMax[k - 1] - 1) + g(n - rollMax[k - 1] - 1, k)
            g_cache[n, k] = ans
            return ans

        def f(n):
            if n < 0:
                return 0
            if n == 0:
                return 1
            if n in f_cache:
                return f_cache[n]
            ans = sum([g(n, k) for k in range(1, 7)])
            f_cache[n] = ans
            return ans
        g_cache = {}
        f_cache = {}
        return f(n) % (10 ** 9 + 7)
