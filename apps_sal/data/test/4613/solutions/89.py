N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]


class Union_Find:
    def __init__(self, n):
        self.par = [-1] * n
        self.siz = [1] * n

    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            return self.root(self.par[x])

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return False

        if self.siz[x] < self.siz[y]:
            tmp = x
            x = y
            y = tmp

        self.par[y] = x
        self.siz[x] += self.siz[y]
        return True

    def size(self, x):
        return self.siz[x]


ans = 0
for m in range(M):
    uf = Union_Find(N)
    for i in range(M):
        if i == m:
            continue
        
        a, b = AB[i]
        a -= 1
        b -= 1
        uf.unite(a, b)

    ans += len(set([uf.root(x) for x in range(N)])) != 1

print(ans)
