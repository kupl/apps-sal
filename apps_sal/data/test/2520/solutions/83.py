class UnionFind():
    def __init__(self, n):
        self.parents = [-1]*n
    
    def root(self, x):
        if self.parents[x] < 0:
            return x
        else:
            return self.root(self.parents[x])
    
    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        else:
            if x > y:
                x, y = y, x
            self.parents[x] += self.parents[y]
            self.parents[y] = x
            return

n, m, k = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
cd = [list(map(int, input().split())) for _ in range(k)]

u = UnionFind(n)
f = [set() for _ in range(n)]
l = [set() for _ in range(n)]
for a, b in ab:
    a, b = a-1, b-1
    f[a].add(b)
    f[b].add(a)
    u.unite(a, b)
for c, d in cd:
    c, d = c-1, d-1
    l[c].add(d)
    l[d].add(c)
ans = [0] * n
for i in range(n):
    r = u.root(i)
    bl = 0
    for j in l[i]:
        if u.root(j) == r:
            bl += 1
    ans[i] = -u.parents[r] - len(f[i]) - bl - 1
print(*ans)
