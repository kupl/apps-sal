from sys import setrecursionlimit
setrecursionlimit(10 ** 9)

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.d = [-1] * n

    def find(self, x):
        if self.d[x] < 0:
            return x
        else:
            self.d[x] = self.find(self.d[x])
            return self.d[x]
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return False
        else:
            if self.d[x] > self.d[y]:
                x, y = y, x
            self.d[x] += self.d[y]
            self.d[y] = x
            return True

    def same(self, x, y):
        return self.find(x) == self.find(y)


    def size(self, x):
        return -self.d[self.find(x)]



MOD = 998244353
def permutations(N):
    val = 1
    for i in range(2,N+1):
        val *= i
        val %= MOD
    return val

N,K = list(map(int,input().split()))
a = [list(map(int,input().split())) for _ in range(N)]

ufretu = UnionFind(N)
for i in range(N):
    for j in range(i+1,N):
        flg = True
        for k in range(N):
            if a[k][i] + a[k][j] > K:
                flg = False
        if flg == True:ufretu.unite(i,j)
val1 = 1
for i in ufretu.d:
    if i < 0:
        val1 *= permutations(-i)
        val1 %= MOD

ufgyou = UnionFind(N)
for i in range(N):
    for j in range(i+1,N):
        flg = True
        for k in range(N):
            if a[i][k] + a[j][k] > K:
                flg = False
        if flg == True:ufgyou.unite(i,j)
val2 = 1
for i in ufgyou.d:
    if i < 0:
        val2 *= permutations(-i)
        val2 %= MOD
print((val1 * val2 % MOD))


