class UnionFind:

    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
        self.size = [1] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            if not self.same_check(x, y):
                self.size[y] += self.size[x]
                self.size[x] = 0
            self.par[x] = y
        else:
            if not self.same_check(x, y):
                self.size[x] += self.size[y]
                self.size[y] = 0
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def siz(self, x):
        x = self.find(x)
        return self.size[x]


(N, K) = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
UFX = UnionFind(N)
UFY = UnionFind(N)
mod = 998244353
fact = [1]
for i in range(1, N + 1):
    fact.append(fact[-1] * i)
for i in range(1, N):
    for j in range(i):
        flag = True
        for k in range(N):
            if A[k][i] + A[k][j] > K:
                flag = False
                break
        if flag:
            UFY.union(i, j)
        flag = True
        for k in range(N):
            if A[i][k] + A[j][k] > K:
                flag = False
                break
        if flag:
            UFX.union(i, j)
ans = 1
for i in range(N):
    if UFX.find(i) == i:
        ans *= fact[UFX.siz(i)]
        ans %= mod
    if UFY.find(i) == i:
        ans *= fact[UFY.siz(i)]
        ans %= mod
print(ans)
