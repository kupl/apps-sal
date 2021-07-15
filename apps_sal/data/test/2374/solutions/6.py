from bisect import bisect_left, bisect_right

from sys import setrecursionlimit
setrecursionlimit(10 ** 6)

class UnionFind:
    def __init__(self, size):
        self.data = [-1] * size
    def find(self, x):
        if self.data[x] < 0:
            return x
        else:
            self.data[x] = self.find(self.data[x])
            return self.data[x]
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x != y:
            if self.data[y] < self.data[x]:
                x, y = y, x
            self.data[x] += self.data[y]
            self.data[y] = x
        return (x != y)
    def same(self, x, y):
        return (self.find(x) == self.find(y))
    def size(self, x):
        return -self.data[self.find(x)]



N, M, *I = map(int, open(0).read().split())
AB, LR = I[:2 * N], I[2 * N:]

A, B = map(list, zip(*sorted(zip(*[iter(AB)] * 2))))
D = [l ^ r for l, r in zip([0] + B, B + [0])]
E = [set() for _ in range(N + 1)]

uf = UnionFind(N + 1)
for i, (l, r) in enumerate(zip(*[iter(LR)] * 2), 1):
    li = bisect_left(A, l)
    ri = bisect_right(A, r)
    if li == ri or uf.same(li, ri):
        continue

    uf.union(li, ri)
    E[li].add((ri, i))
    E[ri].add((li, i))


used = set()
def dfs(v, p):
    res = D[v]
    for u, c in E[v]:
        if u == p:
            continue
        ret = dfs(u, v)
        if ret == 1:
            used.add(c)
        D[u] = 0
        res ^= ret
    return res

for v in range(N + 1):
    if D[v]:
        D[v] = dfs(v, -1)

if all(d == 0 for d in D):
    print(len(used))
    print(*sorted(used))
else:
    print(-1)
