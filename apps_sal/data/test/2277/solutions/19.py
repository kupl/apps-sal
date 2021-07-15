import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**15
mod = 10**9+7

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
    a = LI()
    q = I()
    b = [LI() for _ in range(q)]
    t = 0
    for i in range(n):
        for j in range(i+1,n):
            if a[i] > a[j]:
                t += 1
    r = []
    for c,d in b:
        k = d-c+1
        if k*(k-1)//2 % 2 == 1:
            t += 1
        if t % 2 == 0:
            r.append('even')
        else:
            r.append('odd')

    return '\n'.join(r)

print(main())



