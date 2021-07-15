import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import time,random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
mod2 = 998244353
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def pe(s): return print(str(s), file=sys.stderr)
def JA(a, sep): return sep.join(map(str, a))
def JAA(a, s, t): return s.join(t.join(map(str, b)) for b in a)


def main():
    n,a,b,c = LI()
    t = [a,b,c]
    q = [S() for _ in range(n)] + ["ABC"]
    r = []
    for qi in range(n):
        s = q[qi]
        if s == "AB":
            i = 0
            j = 1
        elif s == "AC":
            i = 0
            j = 2
        else:
            i = 1
            j = 2

        if t[i] < t[j]:
            r.append(i)
            t[i] += 1
            t[j] -= 1
        elif t[i] > t[j]:
            r.append(j)
            t[i] -= 1
            t[j] += 1
        else:
            if t[i] < 1:
                return "No"
            if chr(ord("A") + i) in q[qi+1]:
                r.append(i)
                t[i] += 1
                t[j] -= 1
            else:
                r.append(j)
                t[i] -= 1
                t[j] += 1

    return JA(["Yes"] + list(map(lambda x: chr(ord("A") + x), r)), "\n")

print(main())




