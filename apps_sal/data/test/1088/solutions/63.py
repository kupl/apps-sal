class UnionFind:

    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, v):
        if self.parents[v] < 0:
            return v
        else:
            self.parents[v] = self.find(self.parents[v])
            return self.parents[v]

    def unite(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return
        if self.parents[u] > self.parents[v]:
            (u, v) = (v, u)
        self.parents[u] += self.parents[v]
        self.parents[v] = u

    def size(self, v):
        return -self.parents[self.find(v)]

    def same(self, u, v):
        return self.find(u) == self.find(v)


def comb_lists(n, mod):
    fact = [1 for _ in range(n + 1)]
    inv = [1 for _ in range(n + 1)]
    fact_inv = [1 for _ in range(n + 1)]
    for i in range(2, n + 1):
        fact[i] = fact[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        fact_inv[i] = fact_inv[i - 1] * inv[i] % mod
    return (fact, fact_inv)


mod = 998244353
(N, K) = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
uf_c = UnionFind(N)
uf_r = UnionFind(N)
for i in range(N):
    for j in range(i + 1, N):
        f = True
        for k in range(N):
            if A[i][k] + A[j][k] > K:
                f = False
                break
        if f:
            uf_c.unite(i, j)
for i in range(N):
    for j in range(i + 1, N):
        f = True
        for k in range(N):
            if A[k][i] + A[k][j] > K:
                f = False
                break
        if f:
            uf_r.unite(i, j)
(fact, _) = comb_lists(N, mod)
ps = []
ans = 1
for i in range(N):
    p = uf_c.find(i)
    if p not in ps:
        ans *= fact[uf_c.size(i)]
        ans %= mod
        ps.append(p)
ps = []
for i in range(N):
    p = uf_r.find(i)
    if p not in ps:
        ans *= fact[uf_r.size(i)]
        ans %= mod
        ps.append(p)
print(ans)
