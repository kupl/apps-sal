class UnionFind:

    def __init__(self, N):
        self.root = list(range(N))
        self.size = [1] * N

    def find_root(self, x):
        root = self.root
        while root[x] != x:
            root[x] = root[root[x]]
            x = root[x]
        return x

    def merge(self, x, y):
        x = self.find_root(x)
        y = self.find_root(y)
        if x == y:
            return
        (sx, sy) = (self.size[x], self.size[y])
        if sx < sy:
            self.root[x] = y
            self.size[y] += sx
        else:
            self.root[y] = x
            self.size[x] += sy


(n, m) = map(int, input().split())
xyz = []
for i in range(m):
    xyz.append(list(map(int, input().split())))
uf = UnionFind(n)
answer = []
find_root = uf.find_root
merge = uf.merge
for i in range(m):
    (x, y, z) = (xyz[i][0] - 1, xyz[i][1] - 1, xyz[i][2])
    merge(x, y)
s = set([])
for i in range(n):
    s.add(uf.find_root(i))
print(len(s))
