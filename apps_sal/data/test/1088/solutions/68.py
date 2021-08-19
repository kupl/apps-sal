from collections import defaultdict


class DisjoinSet:

    def __init__(self, N):
        self.par = [-1] * N
        self.sz = [1] * N

    def root(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def unite(self, a, b):
        a = self.root(a)
        b = self.root(b)
        if a == b:
            return
        if self.sz[a] > self.sz[b]:
            (a, b) = (b, a)
        self.par[a] = b
        self.sz[b] += self.sz[a]

    def same(self, a, b):
        return self.root(a) == self.root(b)

    def size(self, x):
        return self.sz[self.root(x)]

    def groups(self):
        clusters = defaultdict(list)
        for x in range(N):
            clusters[self.root(x)].append(x)
        return list(clusters.values())


(N, K) = list(map(int, input().split()))
M = 998244353
A = [[int(x) for x in input().split()] for _ in range(N)]
fact = [1] * (N + 1)
for i in range(1, N + 1):
    fact[i] = fact[i - 1] * i % M
row_dsu = DisjoinSet(N)
for r1 in range(N):
    for r2 in range(r1, N):
        if all((A[r1][c] + A[r2][c] <= K for c in range(N))):
            row_dsu.unite(r1, r2)
col_dsu = DisjoinSet(N)
for c1 in range(N):
    for c2 in range(c1, N):
        if all((A[r][c1] + A[r][c2] <= K for r in range(N))):
            col_dsu.unite(c1, c2)
cntR = 1
for group in row_dsu.groups():
    cntR = cntR * fact[len(group)] % M
cntC = 1
for group in col_dsu.groups():
    cntC = cntC * fact[len(group)] % M
print(cntR * cntC % M)
