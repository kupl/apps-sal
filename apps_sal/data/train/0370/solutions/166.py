class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        par = [-1] * 100001

        def _find(x):
            if par[x] == -1:
                return x
            par[x] = _find(par[x])
            return par[x]

        def _union(x, y):
            xp = _find(x)
            yp = _find(y)
            if xp != yp:
                par[yp] = xp
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
