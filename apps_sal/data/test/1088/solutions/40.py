import numpy as np


class UnionFind:
    def __init__(self, N):
        self.root = list(range(N + 1))
        self.size = [1] * (N+1)


    def __getitem__(self, x):
        root = self.root
        while root[x] != x:
            root[x] = root[root[x]]
            x = root[x]
        return x

    def merge(self, x, y):
        x = self[x]
        y = self[y]
        if x == y:
            return
        sx, sy = self.size[x], self.size[y]
        if sx < sy:
            x, y = y, x
            sx, sy = sy, sx
        self.root[y] = x
        self.size[x] += sy
        self.size[y] = 0

    def same(self, x, y):
        return self[x] == self[y]

    def find_max(self):
        return max(self.size)


N, K = list(map(int, input().split()))
A = np.array([list(map(int, input().split())) for _ in range(N)], dtype=np.int64)
ans = 1
# rows and columns
for step in range(2):
    if step == 1:
        A = A.T

    uf = UnionFind(N)
    merge = uf.merge
    same = uf.same
    comb = 1

    # swap ok?
    for i in range(N):
        for j in range(i+1, N):
            if np.all(A[i, :] + A[j, :] <= K):
                merge(i+1, j+1)

    # prod of tree-size!
    for i in uf.size:
        comb *= np.math.factorial(i)
        comb %= 998244353

    ans *= comb
    ans %= 998244353

print(ans)

