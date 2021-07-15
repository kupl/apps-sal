from heapq import heappush, heappop


class UnionFind():
    def __init__(self, n):
        self.parents = list(range(n))

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.parents[y] = x

N = int(input())
q = []
ans = 0
S = UnionFind(N)
x = []
y = []

for i in range(N):
    p,r = map(int, input().split())
    x.append([p,i])
    y.append([r,i])

x.sort()
y.sort()
for i in range(N-1):
    x1, i1 = x[i]
    y1, j1 = y[i]
    x2, i2 = x[i+1]
    y2, j2 = y[i+1]
    heappush(q, (abs(x1-x2), i1, i2))
    heappush(q, (abs(y1-y2), j1, j2))

heappush(q, (abs(x[N-1][0]-x[0][0]), x[N-1][1], x[0][1]))
heappush(q, (abs(y[N-1][0]-y[0][0]), y[N-1][1], y[0][1]))
# クラスカル法
while len(q) > 0:
    d, a, b = heappop(q)
    if S.find(a) != S.find(b):
        ans += d
        S.union(a, b)
print(ans)
