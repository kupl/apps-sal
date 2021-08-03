class UnionFind:
    def __init__(self, n):
        self.roots = [i for i in range(n)]
        self.sizes = [1 for i in range(n)]

    def root(self, a):
        c = a
        while self.roots[c] != c:
            c = self.roots[c]
        self.roots[a] = c
        return c

    def add(self, a, b):
        a = self.root(a)
        b = self.root(b)
        if self.sizes[a] < self.sizes[b]:
            a, b = b, a
        self.roots[b] = a
        self.sizes[a] += self.sizes[b]


class Solution:
    def findLatestStep(self, arr: List[int], M: int) -> int:
        uf = UnionFind(len(arr))
        m = [0 for i in range(len(arr))]
        good = set()
        day = 1
        result = -1
        for a in arr:
            a -= 1
            m[a] = 1

            if a > 0 and m[a - 1] == 1:
                if uf.root(a - 1) in good:
                    good.remove(uf.root(a - 1))
                uf.add(a, a - 1)
            if a < len(arr) - 1 and m[a + 1] == 1:
                if uf.root(a + 1) in good:
                    good.remove(uf.root(a + 1))
                uf.add(a, a + 1)
            if uf.sizes[uf.root(a)] == M:
                good.add(uf.root(a))
            if good:
                result = day
            day += 1
        return result
