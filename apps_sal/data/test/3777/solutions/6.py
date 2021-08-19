import sys


class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def root(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def merge(self, x, y):
        (x, y) = (self.root(x), self.root(y))
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            (x, y) = (y, x)
        self.size[x] += self.size[y]
        self.parent[y] = x
        return True

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def getsize(self, x):
        return self.size[self.root(x)]


def largest(U, V):
    order = []
    st = [U]
    parent = [-1] * n
    wt = [0] * n
    while st:
        v = st.pop()
        if v == V:
            break
        order.append(v)
        for (c, d) in g[v]:
            if c != parent[v]:
                st.append(c)
                parent[c] = v
                wt[c] = d
    res = 0
    while V != U:
        res = max(res, wt[V])
        V = parent[V]
    return res


readline = sys.stdin.readline
read = sys.stdin.read
(n, m) = list(map(int, readline().split()))
(x,) = list(map(int, readline().split()))
uvw = [list(map(int, readline().split())) for _ in range(m)]
MOD = 10 ** 9 + 7
p2 = [1]
for _ in range(3000):
    p2.append(p2[-1] * 2 % MOD)
res = []
uvw.sort(key=lambda x: x[2])
UF = UnionFind(n)
wt = 0
g = [[] for _ in range(n)]
for i in range(m):
    (u, v, w) = uvw[i]
    if UF.merge(u - 1, v - 1):
        g[u - 1].append((v - 1, w))
        g[v - 1].append((u - 1, w))
        wt += w
    else:
        res.append(i)
ans = (p2[n - 1] - 2) * p2[m - n + 1] % MOD if wt == x else 0
free = m - n
res2 = []
for idx in res:
    (u, v, w) = uvw[idx]
    L = largest(u - 1, v - 1)
    res2.append(wt + w - L)
res2.sort()
free = m - n
for val in res2:
    if val == x:
        ans += 2 * p2[free]
    free -= 1
print(ans % MOD)
