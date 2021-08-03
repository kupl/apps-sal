class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        parent = [-1] * 100000

        def _find(x):
            if parent[x - 1] == -1:
                return x

            parent[x - 1] = _find(parent[x - 1])
            return parent[x - 1]

        def _union(x, y):
            xp = _find(x)
            yp = _find(y)

            if xp != yp:
                parent[yp - 1] = xp

        for x in A:
            for i in range(2, int(sqrt(x)) + 1):
                if x % i == 0:
                    _union(i, x)
                    _union(x, x // i)

        cache = {}

        for x in A:
            xp = _find(x)
            cache[xp] = 1 + cache.get(xp, 0)

        cache1 = sorted(list(cache.items()), key=lambda x: x[1])
        maxi = cache1[-1][0]

        return cache[maxi]
