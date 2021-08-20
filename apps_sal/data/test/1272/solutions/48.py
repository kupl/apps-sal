import sys
input = sys.stdin.readline


class UnionFind:

    def __init__(self, n):
        self.rank = [0] * n
        self.par = list(range(n))
        self._size = [1] * n

    def find(self, x):
        ch = []
        while self.par[x] != x:
            ch.append(x)
            x = self.par[x]
        for c in ch:
            self.par[c] = x
        return x

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return
        if self.rank[rx] >= self.rank[ry]:
            self.par[ry] = rx
            self._size[rx] += self._size[ry]
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1
        else:
            self.par[rx] = ry
            self._size[ry] += self._size[rx]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return self._size[self.find(x)]


(N, M) = [int(x) for x in input().split()]
E = [tuple((int(x) - 1 for x in input().split())) for _ in range(M)]
inconv = [0] * M
inconv[M - 1] = N * (N - 1) // 2
uf = UnionFind(N)
for i in range(M - 1, 0, -1):
    a = E[i][0]
    b = E[i][1]
    inconv[i - 1] = inconv[i]
    if uf.same(a, b):
        continue
    inconv[i - 1] -= uf.size(a) * uf.size(b)
    uf.union(a, b)
for i in range(M):
    print(inconv[i])
