class UnionFind:

    def __init__(self, n):
        self.table = [-1] * n

    def _root(self, x):
        stack = []
        tbl = self.table
        while tbl[x] >= 0:
            stack.append(x)
            x = tbl[x]
        for y in stack:
            tbl[y] = x
        return x

    def find(self, x, y):
        return self._root(x) == self._root(y)

    def union(self, x, y):
        r1 = self._root(x)
        r2 = self._root(y)
        if r1 == r2:
            return
        d1 = self.table[r1]
        d2 = self.table[r2]
        if d1 <= d2:
            self.table[r2] = r1
            if d1 == d2:
                self.table[r1] -= 1
        else:
            self.table[r1] = r2


(n, m) = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
G = UnionFind(n)
CD = []
for _ in range(m):
    (c, d) = list(map(int, input().split()))
    G.union(c - 1, d - 1)
ansA = [0] * n
ansB = [0] * n
for i in range(n):
    ansA[G._root(i)] += A[i]
    ansB[G._root(i)] += B[i]
if ansA == ansB:
    print('Yes')
else:
    print('No')
