class union_find():
    def __init__(self, n):
        # self.n = n
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


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if sum(a) != sum(b):
    print('No')
    return

g = union_find(n)
for _ in range(m):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    g.unite(c, d)


aa = [0] * n
bb = [0] * n
for i in range(n):
    j = g.find_root(i)
    aa[j] += a[i]
    bb[j] += b[i]

if aa == bb:
    print('Yes')
else:
    print('No')
