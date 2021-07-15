import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

class UnionFind:
    def __init__(self, n):
        self.state = [-1] * n
        #self.size_table = [1<<i for i in range(n)]
        # cntはグループ数
        # self.cnt = n

    def root(self, u):
        v = self.state[u]
        if v < 0: return u
        self.state[u] = res = self.root(v)
        return res

    def merge(self, u, v):
        ru = self.root(u)
        rv = self.root(v)
        if ru == rv: return
        du = self.state[ru]
        dv = self.state[rv]
        if du > dv: ru, rv = rv, ru
        if du == dv: self.state[ru] -= 1
        self.state[rv] = ru
        # self.cnt -= 1
        #self.size_table[ru] |= self.size_table[rv]
        #self.size_table[rv]=0
        return

def main():
    n,k,l=MI()
    road=UnionFind(n)
    train=UnionFind(n)
    for _ in range(k):
        u,v=MI1()
        road.merge(u,v)
    for _ in range(l):
        u,v=MI1()
        train.merge(u,v)
    cnt=defaultdict(int)
    for u in range(n):
        cnt[road.root(u),train.root(u)]+=1
    ans=[cnt[road.root(u),train.root(u)] for u in range(n)]
    print(*ans)

main()

