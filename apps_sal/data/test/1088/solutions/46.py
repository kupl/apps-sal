from math import factorial

class UnionFind:
    def __init__(self, n):
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        x = self.find(x)
        return -self.parents[x]

n, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

mod = 998244353

UF_h = UnionFind(n)
UF_w = UnionFind(n)

for i in range(n-1):
    for j in range(i, n):
        flag = True
        for l in range(n):
            if A[i][l] + A[j][l] > k:
                flag = False
                break

        if flag:
            UF_h.union(i, j)

for i in range(n-1):
    for j in range(i, n):
        flag = True
        for l in range(n):
            if A[l][i] + A[l][j] > k:
                flag = False
                break

        if flag:
            UF_w.union(i, j)

Dh = {UF_h.find(i):UF_h.size(i) for i in range(n)}
Dw = {UF_w.find(i):UF_w.size(i) for i in range(n)}

ans = 1
for i in Dh:
    ans *= factorial(Dh[i])
    ans %= mod
for i in Dw:
    ans *= factorial(Dw[i])
    ans %= mod

print(ans)
