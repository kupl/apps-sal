class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        parent = [-1] * 100001

        def _find(x):
            if parent[x] == -1:
                return x
            parent[x] = _find(parent[x])
            return parent[x]

        def _union(x, y):
            xp = _find(x)
            yp = _find(y)
            if xp != yp:
                parent[yp] = xp
        for x in A:
            for i in range(2, int(sqrt(x)) + 1):
                if x % i == 0:
                    _union(i, x)
                    _union(x, x // i)
        count = 0
        cache = {}
        for x in A:
            xp = _find(x)
            count = max(count, 1 + cache.get(xp, 0))
            cache[xp] = 1 + cache.get(xp, 0)
        return count
