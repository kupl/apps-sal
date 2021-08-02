N, M = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))


class UnionFind():
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
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


tree = UnionFind(N)

for i in range(M):
    cd = list(map(int, input().split()))
    cd[0] -= 1
    cd[1] -= 1
    tree.union(cd[0], cd[1])

dict = {}
for i in range(N):
    x = tree.find(i)
    dict.setdefault(x, [])
    dict[x].append(i)

ans = "Yes"
for i in dict:
    asum = 0
    bsum = 0
    for j in dict[i]:
        asum += a[j]
        bsum += b[j]
    if asum != bsum:
        ans = "No"
print(ans)
