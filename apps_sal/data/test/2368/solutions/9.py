import bisect, collections, copy, heapq, itertools, math, string, sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = float('inf')
MOD = 10**9+7
def I(): return int(input())
def F(): return float(input())
def SS(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LSS(): return input().split()

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.par = list(range(n))
        self.rank = [0] * n

    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            r = self.root(self.par[x])
            self.par[x] = r
            return r

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def merge(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        self.par[y] = x
        return True

def resolve():
    N, M = LI()
    a = LI()
    b = LI()
    # 連結成分の合計が等しければ実現可能
    uf = UnionFind(N)
    for _ in range(M):
        c, d = LI_()
        uf.merge(c, d)

    d = collections.defaultdict(list)
    for i in range(N):
        p = uf.root(i)
        d[p].append(i)
    # print(d)
    if [sum([a[j] for j in v]) == sum([b[j] for j in v]) for k, v in list(d.items())].count(False) == 0:
        print('Yes')
    else:
        print('No')

def __starting_point():
    resolve()

__starting_point()
