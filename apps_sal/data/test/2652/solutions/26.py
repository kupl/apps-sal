class UnionFind:

    def __init__(self, n):
        self.n = n
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

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for (i, x) in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join(('{}: {}'.format(r, self.members(r)) for r in self.roots()))


N = int(input())
G = []
for i in range(N):
    (x, y) = list(map(int, input().split()))
    G.append((x, y, i))
Gx = sorted(G, key=lambda x: x[0])
Gy = sorted(G, key=lambda x: x[1])
newG = []
for i in range(N - 1):
    now = Gx[i]
    next = Gx[i + 1]
    dist = abs(now[0] - next[0])
    newG.append((dist, now[2], next[2]))
for i in range(N - 1):
    now = Gy[i]
    next = Gy[i + 1]
    dist = abs(now[1] - next[1])
    newG.append((dist, now[2], next[2]))
newG.sort()
uf = UnionFind(N)
count = N
ans = 0
for (c, i, j) in newG:
    if count == 0:
        break
    if not uf.same(i, j):
        ans += c
        uf.union(i, j)
        count -= 1
print(ans)
