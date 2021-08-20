class UnionFind:

    def __init__(self, n):
        self.parents = [-1] * n

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
        if x > y:
            (x, y) = (y, x)
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        return


(n, m) = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)][::-1]
u = UnionFind(n)
ans = [n * (n - 1) // 2]
for (a, b) in ab:
    (a, b) = (a - 1, b - 1)
    (ra, rb) = (u.root(a), u.root(b))
    p = u.parents[ra] * u.parents[rb] if ra != rb else 0
    ans.append(ans[-1] - p)
    u.unite(a, b)
ans.pop()
for i in ans[::-1]:
    print(i)
