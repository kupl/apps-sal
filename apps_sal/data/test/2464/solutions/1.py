class UnionFind:
    def __init__(self, N):
        self.par = [i for i in range(N)]
        self.rank = [1 for i in range(N)]
        self.rank[0] = 0

    def union(self, x, y):
        if not self.is_same_set(x, y):
            par_x = self.find_par(x)
            par_y = self.find_par(y)

            if self.rank[par_x] > self.rank[par_y]:
                self.rank[par_x] += self.rank[par_y]
                self.rank[par_y] = 0
                self.par[par_y] = par_x
            else:
                self.rank[par_y] += self.rank[par_x]
                self.rank[par_x] = 0
                self.par[par_x] = par_y

    def find_par(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.find_par(self.par[x])
        return self.par[x]

    def is_same_set(self, x, y):
        return self.find_par(x) == self.find_par(y)

    def size(self, x):
        return self.rank[self.find_par(x)]


n = int(input())

adj = [[] for i in range(n + 1)]

uf0 = UnionFind(n + 1)
uf1 = UnionFind(n + 1)

for i in range(n - 1):
    x, y, c = list(map(int, input().split()))

    if c == 0:
        uf0.union(x, y)
    else:
        uf1.union(x, y)
    adj[x].append(y)
    adj[y].append(x)

    uf0.find_par(x)
    uf1.find_par(y)

resp = 0

resp += sum([uf0.rank[i] * (uf0.rank[i] - 1) for i in set(uf0.par)])
resp += sum([uf1.rank[i] * (uf1.rank[i] - 1) for i in set(uf1.par)])
for i in range(len(uf0.par)):
    if uf0.rank[uf0.find_par(i)] > 1:
        if uf1.rank[uf1.find_par(i)] > 1:
            resp += (uf0.rank[uf0.find_par(i)] - 1) * (uf1.rank[uf1.find_par(i)] - 1)
print(resp)
