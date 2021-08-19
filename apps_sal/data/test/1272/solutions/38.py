import sys
stdin = sys.stdin
inf = 1 << 60
mod = 1000000007
sys.setrecursionlimit(10 ** 7)


def ni():
    return int(ns())


def nin(y):
    return [ni() for _ in range(y)]


def na():
    return list(map(int, stdin.readline().split()))


def nan(y):
    return [na() for _ in range(y)]


def nf():
    return float(ns())


def nfn(y):
    return [nf() for _ in range(y)]


def nfa():
    return list(map(float, stdin.readline().split()))


def nfan(y):
    return [nfa() for _ in range(y)]


def ns():
    return stdin.readline().rstrip()


def nsn(y):
    return [ns() for _ in range(y)]


def ncl(y):
    return [list(ns()) for _ in range(y)]


def nas():
    return stdin.readline().split()


class UnionFind:

    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self._size = [1 for _ in range(n)]
        self._edges = 0

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self._size[y] += self._size[x]
            self._edges += 1
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self._size[x] += self._size[y]
            self._edges += 1

    def size(self, x):
        x = self.find(x)
        return self._size[x]

    def trees(self):
        return self.n - self._edges

    def same(self, x, y):
        return self.find(x) == self.find(y)


(n, m) = na()
ab = nan(m)
ab.reverse()
uf = UnionFind(n)
cur = n * (n - 1) // 2
ans = [cur]
for i in range(m - 1):
    (a, b) = ab[i]
    a -= 1
    b -= 1
    p = uf.size(a)
    q = uf.size(b)
    if uf.same(a, b):
        p = 0
    uf.unite(a, b)
    cur -= p * q
    ans.append(cur)
ans.reverse()
print(*ans, sep='\n')
