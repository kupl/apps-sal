from collections import deque


class ModCalc:
    mod = 10**9 + 7

    def __init__(self, n):
        self.n = n
        self.inv = [1] * (self.n + 1)
        self.fac = [1] * (self.n + 1)
        self.finv = [1] * (self.n + 1)
        self.inv[0] = 0
        self.inv_table()

    def inv_table(self):
        for i in range(2, self.n + 1):
            self.inv[i] = self.inv[self.mod % i] * (self.mod - self.mod // i) % self.mod
            self.fac[i] = self.fac[i - 1] * i % self.mod
            self.finv[i] = self.finv[i - 1] * self.inv[i] % self.mod

    def comb(self, n, r):
        if n < r:
            return 0
        if n < 0 or r < 0:
            return 0

        return self.fac[n] * self.finv[r] % self.mod * self.finv[n - r] % self.mod

    def perm(self, n, r):
        if n < r:
            return 0
        if n < 0 or r < 0:
            return 0

        return self.fac[n] * self.finv[n - r] % self.mod

    def fact(self, n):
        return self.fac[n]


n, k = map(int, input().split())
tree = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

ans = k
mod = 10**9 + 7
mc = ModCalc(100001)

q = deque([1])
dist = [-1] * (n + 1)
dist[1] = 0
while q:
    now = q.popleft()
    cnt = 0
    for node in tree[now]:
        if dist[node] != -1:
            continue
        cnt += 1
        q.append(node)
        dist[node] = dist[now] + 1

    if dist[now] == 0:
        ans *= mc.comb(k - 1, cnt) * mc.fact(cnt) % mod
        ans %= mod
    else:
        ans *= mc.comb(k - 2, cnt) * mc.fact(cnt) % mod
        ans %= mod

print(ans)
