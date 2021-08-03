class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.sz = [1] * (n)

    def find(self, x):
        if x == self.p[x]:
            return x
        self.p[x] = self.find(self.p[x])
        return self.p[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.sz[x] < self.sz[y]:
            x, y = y, x
        self.p[y] = x
        self.sz[x] += self.sz[y]


class Solution:
    def largestComponentSize(self, a: List[int]) -> int:
        N = max(a) + 1

        idx = [-1] * N
        for i, x in enumerate(a):
            idx[x] = i

        dsu = DSU(N)
        siv = [True] * N

        for i in range(2, N):
            if siv[i]:
                root = idx[i]
                for j in range(2 * i, N, i):
                    siv[j] = False
                    if idx[j] != -1:
                        if root == -1:
                            root = idx[j]
                        dsu.unite(root, idx[j])

        return max(dsu.sz)
