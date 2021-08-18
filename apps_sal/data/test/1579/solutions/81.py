import copy
import collections
import sys
read = sys.stdin.read
NXY = [int(_) for _ in read().split()]
N = NXY[0]
X = NXY[1::2]
Y = NXY[2::2]
xi = {x: i for i, x in enumerate(set(X))}
yj = {y: j for j, y in enumerate(set(Y))}


class UnionFind():
    def __init__(self, size):
        self.dat = list(range(size))
        self.SIZE = [1] * size

    def find(self, x):
        dat = self.dat
        stack = [x]
        while True:
            y = stack[-1]
            if dat[y] != y:
                stack += [dat[y]]
            else:
                break
        for s in stack:
            dat[s] = y
        return y

    def unite(self, x, y):
        is_same = self.is_same
        find = self.find
        SIZE = self.SIZE
        dat = self.dat
        if not is_same(x, y):
            X, Y = find(x), find(y)
            SX, SY = SIZE[X], SIZE[Y]
            if SX > SY:
                m = dat[X] = Y
            else:
                m = dat[Y] = X
            SIZE[m] = SX + SY
            SIZE[X + Y - m] = 0

    def is_same(self, x, y):
        find = self.find
        return find(x) == find(y)

    def scan_uf(self):
        find = self.find
        length = len(self.dat)
        for i in range(length):
            find(i)

    def size(self, x):
        return self.SIZE[self.find(x)]


ufx = UnionFind(len(xi))
ufy = UnionFind(len(yj))
sxy = collections.defaultdict(set)
syx = collections.defaultdict(set)
for x, y in zip(X, Y):
    i = xi[x]
    j = yj[y]
    sxy[i].add(j)
    syx[j].add(i)
sxy2 = copy.deepcopy(sxy)
for sy in list(sxy.values()):
    y1 = sy.pop()
    for y in sy:
        ufy.unite(y1, y)
for sx in list(syx.values()):
    x1 = sx.pop()
    for x in sx:
        ufx.unite(x1, x)
ufx.scan_uf()
ufy.scan_uf()
ans = 0
for x, vx in enumerate(ufx.SIZE):
    if vx:
        vy = ufy.size(sxy2[x].pop())
        ans += vx * vy
print((ans - N))
