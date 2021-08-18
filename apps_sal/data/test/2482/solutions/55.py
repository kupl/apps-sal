from collections import Counter


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        elif self.rank[x] > self.rank[y]:
            self.par[y] = x
        else:
            self.par[y] = x
            self.rank[x] += 1


N, K, L = map(int, input().split())
A = [list(map(int, input().split())) for i in range(K)]
B = [list(map(int, input().split())) for i in range(L)]

road = UnionFind(N)
train = UnionFind(N)

for i in range(K):
    road.union(A[i][0], A[i][1])
for i in range(L):
    train.union(B[i][0], B[i][1])

pair = [(road.find(i), train.find(i)) for i in range(1, N + 1)]


c = Counter(pair)
print(*[c[i] for i in pair])
