class UnionFind:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.components = n

    def root(self, x):
        if self.p[x] == x:
            return x
        else:
            self.p[x] = self.root(self.p[x])
            return self.p[x]

    def unite(self, x, y):
        x, y = self.root(x), self.root(y)
        if x != y:
            self.p[x] = y
            self.components -= 1

    def same(self, x, y):
        return (self.root(x) == self.root(y))


N = int(input())
MAX = 100010
UF = UnionFind(2 * MAX)

for _ in range(N):
    x, y = map(int, input().split())
    UF.unite(x, y + MAX)


cnt_x, cnt_y = [0] * (2 * MAX), [0] * (2 * MAX)

for i in range(MAX):
    cnt_x[UF.root(i)] += 1

for i in range(MAX, 2 * MAX):
    cnt_y[UF.root(i)] += 1

print(sum([cnt_x[i] * cnt_y[i] for i in range(2 * MAX)]) - N)
