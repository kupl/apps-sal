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
            return
        if self.parents[x] > self.parents[y]:
            (x, y) = (y, x)
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]


(N, M) = map(int, input().split())
AB = []
for i in range(M):
    AB.append(list(map(int, input().split())))
S = []
uf = UnionFind(N)
for (a, b) in AB[::-1]:
    if a < b:
        (a, b) = (b, a)
    x = uf.size(a - 1)
    y = uf.size(b - 1)
    uf.union(a - 1, b - 1)
    z = uf.size(a - 1)
    t = z * (z - 1) // 2 - x * (x - 1) // 2 - y * (y - 1) // 2
    if t < 0:
        S.append(0)
    else:
        S.append(t)
ans = 0
for _ in range(M):
    ans += S.pop()
    print(ans)
