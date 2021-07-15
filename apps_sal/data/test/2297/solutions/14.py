import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)


def main():
    n = I()
    aa = [LI() for _ in range(n)]
    r = []
    for a,b in aa:
        al = a + (1-a%2)
        ar = b - (1-b%2)
        sa = (ar-al) // 2 + 1
        tr = -(al+ar) * sa // 2

        bl = a + (a%2)
        br = b - (b%2)
        sb = (br-bl) // 2 + 1
        tr += (bl+br) * sb // 2
        r.append(tr)

    return "\n".join(map(str,r))


print(main())

