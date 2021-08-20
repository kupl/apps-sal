class UnionFind:

    def __init__(self, n):
        self.n = n
        self.root = [-1] * (n + 1)
        self.rnk = [0] * (n + 1)

    def Find_Root(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]

    def Unite(self, x, y):
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        if x == y:
            return
        elif self.rnk[x] > self.rnk[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rnk[x] == self.rnk[y]:
                self.rnk[y] += 1

    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    def Count(self, x):
        return -self.root[self.Find_Root(x)]


(N, M) = map(int, input().split())
glaph = []
for i in range(M):
    (A, B) = map(int, input().split())
    glaph.append((A, B))
glaph.reverse()
ans = []
ans.append(N * (N - 1) // 2)
uf = UnionFind(N)
for (i, v) in enumerate(glaph):
    (a, b) = v
    if uf.isSameGroup(a, b):
        ans.append(ans[i])
    else:
        ans.append(ans[i] - uf.Count(a) * uf.Count(b))
    uf.Unite(a, b)
ans.reverse()
for i in range(1, M + 1):
    print(ans[i])
