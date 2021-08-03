class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        x = defaultdict(list)

        def _locate(n):
            if not x[n]:
                return n
            x[n] = _locate(x[n])
            return x[n]

        def _isCommon(n, m):
            np = _locate(n)
            mp = _locate(m)
            if np != mp:
                x[mp] = np

        for n in A:
            for i in range(2, int(sqrt(n)) + 1):
                if not n % i:
                    _isCommon(i, n)
                    _isCommon(n, n // i)
        c = 0
        cache = {}
        for n in A:
            np = _locate(n)
            c = max(c, 1 + cache.get(np, 0))
            cache[np] = 1 + cache.get(np, 0)
        return c
