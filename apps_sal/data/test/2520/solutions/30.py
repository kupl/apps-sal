

class UnionFind():
    def __init__(self, N):
        self.parents = [-1] * N

    def root(self, x):
        if self.parents[x] < 0:
            return x
        else:
            return self.root(self.parents[x])

    def unite(self, x, y):
        x, y = self.root(x), self.root(y)
        if x == y:
            return
        else:
            if x > y:
                x, y = y, x
            self.parents[x] += self.parents[y]
            self.parents[y] = x
            return


N, M, K = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(M)]
CD = [list(map(int, input().split())) for _ in range(K)]

u = UnionFind(N)
f = [set() for _ in range(N)]

l = [set() for _ in range(N)]

for a, b in AB:
    a, b = a - 1, b - 1

    f[a].add(b)

    f[b].add(a)

    u.unite(a, b)


for c, d in CD:
    c, d = c - 1, d - 1
    l[c].add(d)
    l[d].add(c)

ans = [0] * N
for i in range(N):
    r = u.root(i)
    bl = 0
    for j in l[i]:
        if u.root(j) == r:
            bl += 1

    ans[i] = -u.parents[r] - len(f[i]) - bl - 1
print((' '.join(list(map(str, ans)))))
