class UnionFind():
    def __init__(self, n):
        self.n = n
        self.par = [-1] * n

    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.par[x] > self.par[y]:
            x, y = y, x
        self.par[x] += self.par[y]
        self.par[y] = x


N, K, L = map(int, input().split())
Uni_1 = UnionFind(N)
Uni_2 = UnionFind(N)
D = {}
for _ in range(K):
    p, q = map(int, input().split())
    Uni_1.union(p - 1, q - 1)
for _ in range(L):
    p, q = map(int, input().split())
    Uni_2.union(p - 1, q - 1)
for i in range(N):
    k = (Uni_1.find(i), Uni_2.find(i))
    if k in D.keys():
        D[k] += 1
    else:
        D[k] = 1
for i in range(N):
    print(D[(Uni_1.find(i), Uni_2.find(i))], end=" ")
