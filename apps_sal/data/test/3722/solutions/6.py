import sys

sys.setrecursionlimit(10**6)
int1 = lambda x: int(x)-1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI1(): return map(int1, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def BI(): return sys.stdin.readline().rstrip().encode()
def SI(): return sys.stdin.readline().rstrip()
dij = [(0, 1), (-1, 0), (0, -1), (1, 0)]
inf = 10**16
# md = 998244353
md = 10**9+7

from functools import lru_cache

@lru_cache(maxsize=None)
def f(a):
    if a==1 or a==0:return 1
    return (f(a-1)+f(a-2))%md

def solve():
    if n<4:return 1
    if ab == "A":
        if aa == "A":
            return 1
        if ba=="A":
            return f(n-2)
        return pow(2,n-3,md)
    else:
        if bb == "B":
            return 1
        if ba=="B":
            return f(n-2)
        return pow(2,n-3,md)

n=II()
aa=SI()
ab=SI()
ba=SI()
bb=SI()
print(solve())

