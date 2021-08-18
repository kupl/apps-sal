class union_find():
    def __init__(self, n):
        self.root = [-1] * (n + 1)
        self.rank = [0] * (n + 1)
        self.siz = n

    def find_root(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find_root(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        x = self.find_root(x)
        y = self.find_root(y)
        if x == y:
            return
        elif self.rank[x] > self.rank[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
        self.siz -= 1

    def same(self, x, y):
        return self.find_root(x) == self.find_root(y)

    def size(self):
        return self.siz


n, m = list(map(int, input().split()))

ab = []
for _ in range(m):
    ab.append(list(map(int, input().split())))

g = union_find(n)
ans = 0
for i in range(len(ab)):
    for j in range(len(ab)):
        if i == j:
            continue
        a, b = ab[j]
        g.unite(a, b)

    if g.size() != 1:
        ans += 1
    g = union_find(n)


print(ans)
