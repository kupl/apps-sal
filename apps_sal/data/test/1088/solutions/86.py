mod = 998244353
(N, K) = list(map(int, input().split()))
A = []
for i in range(N):
    a = [int(i) for i in input().split()]
    A.append(a)
memo = [1]
for i in range(1, 52):
    num = memo[-1]
    memo.append(num * i % mod)


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

    def count(self, x):
        return -self.table[self._root(x)]

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
            self.table[r1] += d2
        else:
            self.table[r1] = r2
            self.table[r2] += d1


uni1 = UnionFind(N)
uni2 = UnionFind(N)
for i in range(N - 1):
    for j in range(i + 1, N):
        cur1 = 0
        cur2 = 0
        for k in range(N):
            if A[i][k] + A[j][k] <= K:
                cur1 += 1
            if A[k][i] + A[k][j] <= K:
                cur2 += 1
        if cur1 == N:
            uni1.union(i, j)
        if cur2 == N:
            uni2.union(i, j)
lsnum = []
(set1, set2) = (set(), set())
for i in range(N):
    if uni1._root(i) not in set1:
        lsnum.append(uni1.count(i))
        set1.add(uni1._root(i))
    if uni2._root(i) not in set2:
        lsnum.append(uni2.count(i))
        set2.add(uni2._root(i))
ans = 1
for num in lsnum:
    ans = ans * memo[num] % mod
ans %= mod
print(ans)
