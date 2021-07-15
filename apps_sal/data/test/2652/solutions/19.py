import sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

class UnionFind():
    def __init__(self, n):
        self.n = n
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

    def same(self, x, y):
        return self.find(x) == self.find(y)

def kruskal(es, V):
    es.sort(key=lambda x:x[2])
    uf = UnionFind(V)
    res = 0
    for e in es:
        if not uf.same(e[0], e[1]):
            uf.union(e[0], e[1])
            res += e[2]
    return res

def resolve():
    N = I()
    xy = [LI() for _ in range(N)]

    # 辺の候補は、xyそれぞれでソートした隣同士の点の間のみに絞れる
    xy_x_asc = sorted(enumerate(xy), key=lambda x: x[1][0])
    xy_y_asc = sorted(enumerate(xy), key=lambda x: x[1][1])
    edge = []
    for i in range(N-1):
        xc = xy_x_asc[i][1][0]
        yc = xy_x_asc[i][1][1]
        xyc_num = xy_x_asc[i][0]
        xn = xy_x_asc[i+1][1][0]
        yn = xy_x_asc[i+1][1][1]
        xyn_num = xy_x_asc[i+1][0]
        edge.append([xyc_num, xyn_num, abs(xn-xc)])
    for i in range(N-1):
        xc = xy_y_asc[i][1][0]
        yc = xy_y_asc[i][1][1]
        xyc_num = xy_y_asc[i][0]
        xn = xy_y_asc[i+1][1][0]
        yn = xy_y_asc[i+1][1][1]
        xyn_num = xy_y_asc[i+1][0]
        edge.append([xyc_num, xyn_num, abs(yn-yc)])

    # print(edge)
    mst_cost = kruskal(edge, N)
    print(mst_cost)

def __starting_point():
    resolve()
__starting_point()
