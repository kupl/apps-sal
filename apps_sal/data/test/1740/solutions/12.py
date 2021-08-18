class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.rank = [0 for _ in range(n + 1)]
        self.size = [1] * (n + 1)
        self.group = [[i] for i in range(n + 1)]

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
            self.size[y] += self.size[x]
        else:
            self.parent[y] = x
            self.size[x] += self.size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def merge(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if len(self.group[x]) < len(self.group[y]):
            x, y = y, x
        self.group[x].extend(self.group[y])
        self.group[y] = []
        self.parent[y] = x

    def check_same(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.size[self.find(x)]


N = int(input())
items = []
for i in range(N - 1):
    items.append(tuple(map(int, input().split())))

union_find = UnionFind(N)

for a, b in items:
    union_find.merge(a, b)
ans = union_find.group[union_find.find(1)]
print(*ans)
