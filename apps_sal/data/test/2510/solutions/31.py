class UnionFind():
    def __init__(self, N):
        self.par = [-1] * N

    def root(self, x):
        if self.par[x] < 0: return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        #print(f'root: {rx} {ry}')
        if rx == ry: return

        self.par[ry] += self.par[rx]
        self.par[rx] = ry


N, M = map(int, input().split())
uf = UnionFind(N)
for i in range(M):
    A, B = map(lambda x: int(x), input().split())
    A, B = A - 1, B - 1
    #print(f'{A} {B} {uf.par}')
    uf.unite(A, B)
    #print(f'{A} {B} {uf.par}')

print(-min(uf.par))
