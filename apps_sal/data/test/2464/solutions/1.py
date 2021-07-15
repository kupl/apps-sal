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
        if self.par[x] == x: return x
        self.par[x] = self.find_par(self.par[x])
        return self.par[x]

    def is_same_set(self, x, y):
        return self.find_par(x) == self.find_par(y)

    def size(self, x):
        return self.rank[self.find_par(x)]
# 2 unionfind, para 0 e para 1 formando 2 florestas
# lista de adj
# verificar todos os componentes existentes e adicionar na resposta n * (n-1)

n = int(input())

adj = [[] for i in range(n+1)]

uf0 = UnionFind(n+1)
uf1 = UnionFind(n+1)

for i in range(n-1):
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
# pra cada componente do 0-uf verificar se existe esse vertice na 1-uf e ele for conectado com alguém, se sim, multiplicar (n-1)*(m-1) sendo n o componente da 0-uf e m o componente da 1-f e adicionar na resposta
#ja_visto = set()
for i in range(len(uf0.par)):
    if uf0.rank[uf0.find_par(i)] > 1: #and not uf0.find_par(i) in ja_visto:
        #ja_visto.add(uf0.find_par(i))
        if uf1.rank[uf1.find_par(i)] > 1:
            resp += (uf0.rank[uf0.find_par(i)] - 1) * (uf1.rank[uf1.find_par(i)] - 1)
print(resp)

