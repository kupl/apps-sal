from heapq import heapify, heappop, heappush
N, *A = list(map(int, open(0).read().split()))
*A, = list(zip(*[iter(A)] * 2))
A = [(x, y, i) for i, (x, y) in enumerate(A)]
A.sort()
G = []
x0, y0, i0 = A[0]
for x, y, i in A[1:]:
    c = min(abs(x - x0), abs(y - y0))
    heappush(G, (c, i0, i))
    x0, y0, i0 = x, y, i
A.sort(key=lambda x: x[1])
x0, y0, i0 = A[0]
for x, y, i in A[1:]:
    c = min(abs(x - x0), abs(y - y0))
    heappush(G, (c, i0, i))
    x0, y0, i0 = x, y, i


class UnionFind:
    def __init__(self, n=0):
        self.d = [-1] * n
        self.u = n

    def root(self, x):
        if self.d[x] < 0:
            return x
        self.d[x] = self.root(self.d[x])
        return self.d[x]

    def unite(self, x, y):
        x, y = self.root(x), self.root(y)
        if x == y:
            return False
        if x > y:
            x, y = y, x
        self.d[x] += self.d[y]
        self.d[y] = x
        self.u -= 1
        return True

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.d[self.root(x)]

    def num_union(self):
        return self.u


ans = 0
u = UnionFind(N)
while u.num_union() > 1:
    c, a, b = heappop(G)
    if u.same(a, b):
        continue
    u.unite(a, b)
    ans += c

print(ans)
