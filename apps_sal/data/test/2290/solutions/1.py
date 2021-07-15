import sys
input = sys.stdin.readline


class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.cnt = n

    def root(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def merge(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x != y:
            if self.parent[x] > self.parent[y]:
                x, y = y, x
            self.parent[x] += self.parent[y]
            self.parent[y] = x
            self.cnt -= 1
          
    def is_same(self, x, y):
        return self.root(x) == self.root(y)
             
    def get_size(self, x):
        return -self.parent[self.root(x)]
    
    def get_cnt(self):
        return self.cnt



n, m = map(int, input().split())
info = [list(map(int, input().split())) for i in range(m)]
uf = UnionFind(n)

for a, b in info:
    uf.merge(a - 1, b - 1)

ans = 0
i = 0
while True:
    if i >= n:
        break
    cnt = uf.get_size(i)
    j = i
    while cnt:
        if uf.is_same(i, j):
            cnt -= 1
            j += 1
        else:
            cnt -= 1
            cnt += uf.get_size(j)
            ans += 1
            uf.merge(i, j)
            j += 1
    i = j
print(ans)
