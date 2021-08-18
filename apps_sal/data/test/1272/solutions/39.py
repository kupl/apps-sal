from collections import defaultdict
n, m = map(int, input().split())


class UnionFind:
    def __init__(self, n):
        class KeyDict(dict):
            def __missing__(self, key):
                self[key] = key
                return key
        self.parent = KeyDict()
        self.rank = defaultdict(int)
        self.weight = defaultdict(lambda: 1)

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            y = self.find(self.parent[x])
            self.parent[x] = y
            return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
            self.weight[y] += self.weight[x]
            self.weight[x] = 0
        else:
            self.parent[y] = x
            self.weight[x] += self.weight[y]
            self.weight[y] = 0

        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

    def judge(self, x, y):
        return self.find(x) == self.find(y)


ps = []
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ps.append((a, b))

uf = UnionFind(n)
now = n * (n - 1) // 2
ans = [now]
for a, b in ps[::-1]:
    if not uf.judge(a, b):
        n1 = uf.weight[uf.find(a)]
        n2 = uf.weight[uf.find(b)]
        now += n1 * (n1 - 1) // 2 + n2 * (n2 - 1) // 2 - (n1 + n2) * (n1 + n2 - 1) // 2
        uf.union(a, b)
    ans.append(now)

for a in ans[::-1][1:]:
    print(a)
