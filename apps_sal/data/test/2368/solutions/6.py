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

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

uf = UnionFind(n)
for i in range(m):
    c, d = map(int, input().split())
    uf.union(c - 1, d - 1)

sumA = {}
sumB = {}
for i in range(n):
    g = uf.find(i)
    if g in sumA:
        sumA[g] += a[i]
        sumB[g] += b[i]
    else:
        sumA[g] = a[i]
        sumB[g] = b[i]

ans = "Yes"
for k in sumA.keys():
    if sumA[k] != sumB[k]:
        ans = "No"
        break

print(ans)
