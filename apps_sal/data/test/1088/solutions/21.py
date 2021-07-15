from math import factorial

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    
    #要素xが属するグループの根を返す
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    #xのグループとyのグループを併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    #xのグループのサイズ
    def size(self, x):
        return -self.parents[self.find(x)]

n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
mod = 998244353
ans = 1
flag = 1

uf = UnionFind(n)
# 行方向
for r1 in range(n):
    for r2 in range(r1+1, n):
        for c in range(n):
            flag = 1
            if a[r1][c]+a[r2][c] > k:
                flag = 0
                break
        
        if flag:
            uf.union(r1, r2)
for i in range(n):
    if uf.parents[i] < 0:
        ans *= factorial(uf.size(i))
        ans %= mod

uf = UnionFind(n)

# 列
for c1 in range(n):
    for c2 in range(c1+1, n):
        for r in range(n):
            flag = 1
            if a[r][c1]+a[r][c2] > k:
                flag = 0
                break
        if flag:
            uf.union(c1, c2)

for i in range(n):
    if uf.parents[i] < 0:
        ans *= factorial(uf.size(i))
        ans %= mod
print(ans)
