class UnionFind:

    def __init__(self, n):
        self.n = n
        self.p = [-1] * n

    def leader(self, a):
        while self.p[a] >= 0:
            a = self.p[a]
        return a

    def merge(self, a, b):
        x = self.leader(a)
        y = self.leader(b)
        if x == y:
            return x
        if self.p[x] > self.p[y]:
            (x, y) = (y, x)
        self.p[x] += self.p[y]
        self.p[y] = x
        return x


def f():
    return map(int, input().split())


(n, k) = f()
A = [[*f()] for _ in range(n)]
(ufh, ufw) = (UnionFind(n), UnionFind(n))
for y in range(n):
    for x in range(y):
        if all((A[h][x] + A[h][y] <= k for h in range(n))):
            ufw.merge(x, y)
        if all((A[x][w] + A[y][w] <= k for w in range(n))):
            ufh.merge(x, y)
M = 998244353
F = [1]
for i in range(1, 51):
    F += [i * F[-1] % M]
c = 1
for i in range(n):
    if ufh.p[i] < 0:
        c = c * F[-ufh.p[i]] % M
    if ufw.p[i] < 0:
        c = c * F[-ufw.p[i]] % M
print(c)
