class UnionFind():
    def __init__(self, n):
        self.n = n
        self.para = [-1] * (n + 1)

    def find(self, x):
        if self.para[x] < 0:
            return x
        else:
            self.para[x] = self.find(self.para[x])
            return self.para[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x > y:
            x, y = y, x
        if x == y:
            return
        else:
            self.para[x] += self.para[y]
            self.para[y] = x

    def isSame(self, x, y):
        return self.find(x) == self.find(y)

    def count(self, x):
        return -self.para[self.find(x)]


N, M = map(int, input().split())
un_orginal = UnionFind(N)
A = [tuple(map(int, input().split())) for _ in range(M)]
for a, b in A:
    un_orginal.unite(a, b)
ans = 0
for i in range(M):
    un = UnionFind(N)
    for k in range(M):
        if i == k:
            continue
        else:
            un.unite(A[k][0], A[k][1])
    cnt = 0
    for k in range(N + 1):
        if un_orginal.count(k) == un.count(k):
            cnt += 1
    if cnt == N + 1:
        ans += 1
print(M - ans)
