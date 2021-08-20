from itertools import chain


class DisjointSet:

    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        stack = []
        parent = self.parent
        while parent[x] != x:
            stack.append(x)
            x = parent[x]
        for y in stack:
            parent[y] = x
        return x

    def union(self, x, y):
        (xr, yr) = (self.find(x), self.find(y))
        if self.rank[xr] > self.rank[yr]:
            self.parent[yr] = xr
        elif self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        elif xr != yr:
            self.parent[yr] = xr
            self.rank[xr] += 1


N = int(input())
points = tuple((tuple(map(int, input().split())) for _ in range(N)))
ds = DisjointSet(N)
x_i = sorted(((x, i) for (i, (x, y)) in enumerate(points)))
y_i = sorted(((y, i) for (i, (x, y)) in enumerate(points)))
xr = [x_i[0]]
yr = [y_i[0]]
for ((x0, i0), (x1, i1)) in zip(x_i, x_i[1:]):
    if x0 == x1:
        ds.union(i0, i1)
    else:
        xr.append((x1, i1))
for ((y0, i0), (y1, i1)) in zip(y_i, y_i[1:]):
    if y0 == y1:
        ds.union(i0, i1)
    else:
        yr.append((y1, i1))
deltas = sorted(chain(((x1 - x0, i0, i1) for ((x0, i0), (x1, i1)) in zip(xr, xr[1:])), ((y1 - y0, i0, i1) for ((y0, i0), (y1, i1)) in zip(yr, yr[1:]))))


def it():
    for (d, i0, i1) in deltas:
        (i0, i1) = (ds.find(i0), ds.find(i1))
        if i0 != i1:
            ds.union(i0, i1)
            yield d


print(sum(it()))
