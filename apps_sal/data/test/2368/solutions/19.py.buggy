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

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def num_members(self, x):
        return abs(self.parents[self.find(x)])

    def groups(self):
        r_to_g = {}
        cnt = 0
        groups = []
        for i in range(self.n):
            r = self.find(i)
            if r not in r_to_g:
                groups.append([i])
                r_to_g[r] = cnt
                cnt += 1
            else:
                groups[r_to_g[r]].append(i)
        return groups


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
uf = UnionFind(N)
for i in range(M):
    c, d = map(int, input().split())
    uf.union(c - 1, d - 1)
for g in uf.groups():
    cnt = 0
    for v in g:
        cnt += A[v] - B[v]
    if cnt != 0:
        print('No')
        return
print('Yes')
