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


(N, M) = map(int, input().split())
AB = []
for _ in range(M):
    AB.append(list(map(int, input().split())))
ans = 0
for i in range(M):
    if i == M - 1:
        ab = AB[:M - 1]
    else:
        ab = AB[:i] + AB[i + 1:]
    uf = UnionFind(N)
    for j in ab:
        uf.union(j[0] - 1, j[1] - 1)
    if uf.parents[uf.find(0)] != -N:
        ans += 1
print(ans)
