N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]

ab.reverse()
cnt = [0] * N
lst = [0]*N

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            return self.find(self.parents[x])
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y: return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
     
    def size(self, x):
        return -self.parents[self.find(x)]

uf = UnionFind(N)
cnt = N * (N - 1) // 2
ans = [cnt]
for a, b in ab:
    a -= 1
    b -= 1
    if uf.find(a) != uf.find(b):
        cnt -= uf.size(a) * uf.size(b)
        uf.union(a, b)
    ans.append(cnt)
ans.reverse()
print(*ans[1:], sep='\n')
