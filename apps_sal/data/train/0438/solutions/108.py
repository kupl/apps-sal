class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if n == m:
            return m
        fa = [i for i in range(n)]
        sz = [0 for i in range(n)]

        def gf(i) -> int:
            if fa[i] != i:
                fa[i] = gf(fa[i])
            return fa[i]

        def merge(x, y):
            (fx, fy) = (gf(x), gf(y))
            if fx != fy:
                if sz[fx] < sz[fy]:
                    (fx, fy) = (fy, fx)
                fa[fy] = fx
                sz[fx] += sz[fy]
        ans = -1
        for i in range(n):
            a = arr[i] - 1
            sz[a] = 1
            for j in (a - 1, a + 1):
                if 0 <= j < n and sz[j] > 0:
                    if sz[gf(j)] == m:
                        ans = i
                    merge(j, a)
        return ans
