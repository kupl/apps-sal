import heapq


class union_find:

    def __init__(self, N):
        self.par = [-1] * N

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        else:
            if self.par[x] > self.par[y]:
                (x, y) = (y, x)
            self.par[x] += self.par[y]
            self.par[y] = x
            return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.par[self.find(x)]


N = int(input())
XYI = []
for i in range(N):
    (x, y) = map(int, input().split())
    XYI.append((x, y, i))
edges = []
heapq.heapify(edges)
XYI.sort(key=lambda x: x[0])
for j in range(1, N):
    (px, py, pi) = XYI[j - 1]
    (x, y, i) = XYI[j]
    d = min(abs(x - px), abs(y - py))
    heapq.heappush(edges, (d, pi, i))
XYI.sort(key=lambda x: x[1])
for j in range(1, N):
    (px, py, pi) = XYI[j - 1]
    (x, y, i) = XYI[j]
    d = min(abs(x - px), abs(y - py))
    heapq.heappush(edges, (d, pi, i))
uf = union_find(N)
ans = 0
while True:
    (d, i, j) = heapq.heappop(edges)
    if uf.same(i, j):
        continue
    uf.unite(i, j)
    ans += d
    if uf.size(i) == N:
        break
print(ans)
