from itertools import combinations


class DisjointSetUnion():
    def __init__(self, n):
        self.n = n
        self.par_size = [-1] * n

    def merge(self, a, b):
        #assert 0 <= a < self.n
        #assert 0 <= b < self.n
        x = self.leader(a)
        y = self.leader(b)
        if x == y:
            return x
        if -self.par_size[x] < -self.par_size[y]:
            x, y = y, x
        self.par_size[x] += self.par_size[y]
        self.par_size[y] = x
        return x

    def same(self, a, b):
        #assert 0 <= a < self.n
        #assert 0 <= b < self.n
        return self.leader(a) == self.leader(b)

    def leader(self, a):
        #assert 0 <= a < self.n
        x = a
        while self.par_size[x] >= 0:
            x = self.par_size[x]
        while self.par_size[a] >= 0:
            self.par_size[a] = x
            a = self.par_size[a]
        return x

    def size(self, a):
        #assert 0 <= a < self.n
        return -self.par_size[self.leader(a)]


def build_factorial(n):
    fct = [0] * (n + 1)
    inv = [0] * (n + 1)
    fct[0] = inv[0] = 1
    for i in range(n):
        fct[i + 1] = fct[i] * (i + 1) % MOD
    inv[n] = pow(fct[n], MOD - 2, MOD)
    for i in range(n)[::-1]:
        inv[i] = inv[i + 1] * (i + 1) % MOD
    return fct, inv


MOD = 998244353

N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

uf1 = DisjointSetUnion(N)
uf2 = DisjointSetUnion(N)

for i, j in combinations(range(N), 2):
    for k in range(N):
        if A[i][k] + A[j][k] > K:
            break
    else:
        uf1.merge(i, j)

    for k in range(N):
        if A[k][i] + A[k][j] > K:
            break
    else:
        uf2.merge(i, j)

fct, inv = build_factorial(N)
res = 1

for i in range(N):
    if uf1.par_size[i] < 0:
        res *= fct[-uf1.par_size[i]]
        res %= MOD
    if uf2.par_size[i] < 0:
        res *= fct[-uf2.par_size[i]]
        res %= MOD

print(res)
