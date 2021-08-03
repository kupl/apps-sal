import functools

mod = 10 ** 9 + 7


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        def memo(f):
            d = defaultdict()

            def inner(*args):
                if d.get(args) is None:
                    d[args] = f(*args)
                return d[args]
            return inner

        @functools.lru_cache(maxsize=n * n)
        def inner(n, last, last_n):
            if n == 0:
                return 1

            r = list(range(1, 7))

            if last and last_n >= rollMax[last - 1]:
                del r[last - 1]

            res = [
                inner(n - 1, i, 1 if i != last else last_n + 1) for i in r
            ]

            return sum(res)

        return inner(n, None, None) % mod
