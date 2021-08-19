class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def root(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x != y:
            self.parent[x] = y
            self.size[y] += self.size[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def count(self, x):
        return self.size[self.root(x)]


(N, M) = list(map(int, input().split()))
AB = [list([int(x) - 1 for x in input().split()]) for _ in range(M)]
ans = 0
for i in range(M):
    un = UnionFind(N)
    for j in range(M):
        if i != j:
            un.unite(AB[j][0], AB[j][1])
    if un.count(0) != N:
        ans += 1
print(ans)
