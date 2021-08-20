MOD = 998244353
SIZE = 10 ** 6
g1 = [1, 1]
g2 = [1, 1]
re = [0, 1]
for i in range(2, SIZE + 1):
    g1.append(g1[-1] * i % MOD)


def fact(n):
    return g1[n]


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
        elif sx >= sy:
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


(N, K) = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]


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
    for (a, b) in edge:
        uf.union(a, b)
    ret = 1
    sl = uf.size_list(N)
    for n in sl:
        ret = ret * fact(n) % MOD
    return ret


uf = UnionFind(N)
answer = f(A) % MOD
tmp = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        tmp[j].append(A[i][j])
A = tmp
uf = UnionFind(N)
answer = answer * f(A) % MOD
print(answer)
