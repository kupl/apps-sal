class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return self.parents[self.find(x)]


N, M, K = map(int, input().split())
uf = UnionFind(N + 1)
friends = {x: set() for x in range(1, N + 1)}
blocks = {x: set() for x in range(1, N + 1)}
ans = [N - 1] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    friends[A].add(B)
    friends[B].add(A)
    uf.union(A, B)

for _ in range(K):
    C, D = map(int, input().split())
    if uf.find(C) == uf.find(D):
        blocks[C].add(D)
        blocks[D].add(C)

for i in range(1, N + 1):
    if uf.size(i) == -1:
        print(0)
        continue
    print(abs(uf.size(i)) - len(friends[i]) - len(blocks[i]) - 1, end=' ')
