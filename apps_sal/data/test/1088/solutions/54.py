class TwelvefoldWay:
    def __init__(self, n, mod):
        self.g1 = [1, 1]
        self.g2 = [1, 1]
        self.re = [0, 1]
        self.md = mod
        for i in range(2, n + 1):
            self.g1.append((self.g1[-1] * i) % self.md)

    def fact(self, n):
        return self.g1[n]

    def perm(self, n, k):
        return (self.g1[n] * self.g2[n - k]) % self.md

    def comb(n, k):
        if k < 0 or k > n:
            return 0
        k = min(k, n - k)
        return self.g1[n] * self.g2[k] * self.g2[n - k] % self.md

    def homo(n, k):
        return self.comb(n + k - 1, k)


class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)
        self.nn = n

    def find(self, x):
        y = self.root[x]
        if x == y:
            return x
        else:
            z = self.find(y)
            self.root[x] = z
            return z

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        sx = self.size[rx]
        sy = self.size[ry]
        if rx == ry:
            return 0
        else:
            if sx >= sy:
                self.root[ry] = rx
                self.size[rx] = sx + sy
            else:
                self.root[rx] = ry
                self.size[ry] = sx + sy
        return sx * sy

    def size_list(self, n):
        ret = []
        cnt = [0] * (n + 1)
        for i in range(1, n + 1):
            if cnt[self.find(i)] == 0:
                cnt[self.find(i)] = 1
                ret.append(self.size[self.find(i)])
        return ret

    def check(self):
        print([self.find(i) for i in range(1, self.nn + 1)])


N, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
MOD = 998244353


def f(A):
    edge = []
    for i in range(N):
        ai = A[i]
        for j in range(i + 1, N):
            aj = A[j]
            flag = True
            for k in range(N):
                if ai[k] + aj[k] > K:
                    flag = False
                    break
            if flag:
                edge.append([i + 1, j + 1])

    uf = UnionFind(N)
    tw = TwelvefoldWay(N ** 2 + 1, MOD)
    for a, b in edge:
        uf.union(a, b)

    ret = 1
    for n in uf.size_list(N):
        ret = (ret * tw.fact(n)) % MOD

    return ret


answer = f(A) % MOD

A = [[A[i][j] for i in range(N)] for j in range(N)]
answer = (answer * f(A)) % MOD
print(answer)
