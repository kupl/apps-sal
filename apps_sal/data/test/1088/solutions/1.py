import math
N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
mod = 998244353


class DSU:
    def __init__(self, n):
        self.uf = {i: i for i in range(n)}
        self.rank = {i: 1 for i in range(n)}

    def find(self, x):
        if self.uf[x] != x:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] > self.rank[py]:
                px, py = py, px
            self.rank[py] += self.rank[px]
            self.uf[px] = py


row, col = DSU(N), DSU(N)
for i in range(N):
    for j in range(i + 1, N):
        if all(a + b <= K for a, b in zip(A[i], A[j])):
            row.union(i, j)
B = list(zip(*A))
for i in range(N):
    for j in range(i + 1, N):
        if all(a + b <= K for a, b in zip(B[i], B[j])):
            col.union(i, j)
ans = 1
for x in set(row.find(i) for i in range(N)):
    ans *= math.factorial(row.rank[x])
    ans %= mod
for x in set(col.find(i) for i in range(N)):
    ans *= math.factorial(col.rank[x])
    ans %= mod
print(ans)
