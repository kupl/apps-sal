

n, m = list(map(int, input().split()))


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
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return - self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i, in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}


edge = []
for _ in range(m):
    a, b = list(map(int, input().split()))
    edge.append((a - 1, b - 1))

ans = [n * (n - 1) // 2]

uf = UnionFind(n)
for a, b in reversed(edge):
    if not uf.same(a, b):
        ag = uf.size(a)
        bg = uf.size(b)
        uf.union(a, b)
        ans.append(ans[-1] - ag * bg)
    else:
        ans.append(ans[-1])

ans.pop()
for i in reversed(ans):
    print(i)
