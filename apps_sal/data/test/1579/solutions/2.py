from collections import defaultdict


class UnionFind:
    n = 1
    par = [0]
    rnk = [0]

    def __init__(self, size):
        self.n = size
        self.par = [i for i in range(self.n)]
        self.rnk = [0 for i in range(self.n)]

    def find(self, vertex1):
        if self.par[vertex1] == vertex1:
            return vertex1
        else:
            self.par[vertex1] = self.find(self.par[vertex1])
            return self.par[vertex1]

    def unite(self, vertex1, vertex2):
        vertex1 = self.find(vertex1)
        vertex2 = self.find(vertex2)
        if vertex1 == vertex2:
            return
        if self.rnk[vertex1] < self.rnk[vertex2]:
            self.par[vertex1] = vertex2
        else:
            self.par[vertex2] = vertex1
            if self.rnk[vertex1] == self.rnk[vertex2]:
                self.rnk[vertex1] += 1

    def same(self, vetrex1, vertex2):
        return self.find(vetrex1) == self.find(vertex2)


N = int(input())
P = [(i,) + tuple(map(int, input().split())) for i in range(N)]
G = UnionFind(N)
P.sort(key=lambda x: x[1])
for i in range(N - 1):
    if P[i][1] == P[i + 1][1]:
        G.unite(P[i][0], P[i + 1][0])
P.sort(key=lambda x: x[2])
for i in range(N - 1):
    if P[i][2] == P[i + 1][2]:
        G.unite(P[i][0], P[i + 1][0])
P.sort(key=lambda x: x[0])
Dx = defaultdict(set)
Dy = defaultdict(set)
for i in range(N):
    j = G.find(i)
    Dx[j].add(P[i][1])
    Dy[j].add(P[i][2])
ans = -N
for j in Dx:
    ans += len(Dx[j]) * len(Dy[j])
print(ans)
