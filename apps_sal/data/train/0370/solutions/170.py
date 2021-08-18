class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def factors(x):
            sq = int(x**0.5)
            f = set()
            for i in range(2, sq + 1):
                while x % i == 0:
                    x //= i
                    f.add(i)
            if x > 1:
                f.add(x)
            return f

        n = len(A)
        parent = [i for i in range(n)]
        sz = [1] * n
        mp = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[rx] = ry
                sz[ry] += sz[rx]
        for i, a in enumerate(A):
            fs = factors(a)
            for f in fs:
                if f in mp:
                    j = mp[f]
                    union(j, i)
                mp[f] = i
        return max(sz)
