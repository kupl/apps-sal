class UnionFind():
    def __init__(self, n):
        self.n = n
        self.par = [-1] * n

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)

        if(rx == ry):
            return

        if(self.par[rx] > self.par[ry]):
            rx, ry = ry, rx
        self.par[rx] += self.par[ry]
        self.par[ry] = rx

    def root(self, x):
        if(self.par[x] < 0):
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def same(self, x, y):
        if(self.root(x) == self.root(y)):
            return True
        else:
            return False

    def rank(self, x):
        return -1 * self.par[self.root(x)]

    def root_num(self):
        retval = 0
        for i in range(self.n):
            if self.par[i] < 0:
                retval += 1
        return retval

    def set_list(self):
        l = [[-1] for i in range(self.n)]
        for i in range(self.n):
            if self.par[i] < 0:
                l[i].append(i)
            else:
                l[self.root(i)].append(i)
        for i in range(self.n - 1, -1, -1):
            del l[i][0]
            if len(l[i]) == 0:
                del l[i]
        return l


N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
uf = UnionFind(N)
for _ in range(M):
    l = list(map(int, input().split()))
    uf.unite(l[0] - 1, l[1] - 1)

l = uf.set_list()
for i in range(len(l)):
    sumA = 0
    sumB = 0
    for j in range(len(l[i])):
        sumA += a[l[i][j]]
        sumB += b[l[i][j]]
    if sumA != sumB:
        print('No')
        return

print('Yes')
