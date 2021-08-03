n = int(input())
l = []
for i in range(n):
    x, y = list(map(int, input().split()))
    l.append([x, y, i])

lx = sorted(l)
ly = sorted(l, key=lambda x: x[1])

e = []
for i in range(n - 1):
    e.append([lx[i + 1][0] - lx[i][0], lx[i + 1][2], lx[i][2]])
    e.append([ly[i + 1][1] - ly[i][1], ly[i + 1][2], ly[i][2]])


class Unionfind:

    def __init__(self, n):
        self.uf = [-1] * n

    def find(self, x):
        if self.uf[x] < 0:
            return x
        else:
            self.uf[x] = self.find(self.uf[x])
            return self.uf[x]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.uf[x] > self.uf[y]:
            x, y = y, x
        self.uf[x] += self.uf[y]
        self.uf[y] = x

    def size(self, x):
        x = self.find(x)
        return -self.uf[x]


s = set()
u = Unionfind(n)
count = 0
e.sort()
for i in e:
    if not u.same(i[1], i[2]):
        u.union(i[1], i[2])
        s.add(i[1])
        s.add(i[2])
        count += i[0]
print(count)
