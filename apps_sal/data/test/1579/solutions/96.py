class UnionFind:
    def __init__(self, n):
        self.v = [-1 for _ in range(n)]

    def find(self, x):
        if self.v[x] < 0:  # (負)は根
            return x
        else:
            self.v[x] = self.find(self.v[x])
            return self.v[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if -self.v[x] < -self.v[y]:
            x, y = y, x
        self.v[x] += self.v[y]
        self.v[y] = x

    def root(self, x):
        return self.v[x] < 0

    def size(self, x):
        return -self.v[self.find(x)]


mx = 10 ** 5 + 10

n = int(input())

uf = UnionFind(mx * 2)

for _ in range(n):
    x, y = list(map(int, input().split()))
    uf.unite(x, y + mx)

vx = [0] * (mx * 2)
vy = [0] * (mx * 2)

for i in range(mx):
    root = uf.find(i)
    vx[root] += 1

for i in range(mx, mx * 2):
    root = uf.find(i)
    vy[root] += 1

ans = -n
for xx, yy in zip(vx, vy):
    ans += xx * yy
print(ans)

