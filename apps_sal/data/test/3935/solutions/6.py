#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

#A
def A():
    n = I()
    s = S()
    d = defaultdict(lambda : 0)
    for i in s:
        d[i] += 1
    ans = [1]*d["n"]
    d["o"] -= d["n"]
    ans += [0]*d["o"]
    print(*ans)
    return

#B
def B():

    n = I()
    m = LIR(n)
    f = [0]*n
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            f[i] += math.log(m[i][j],10)
    F = sum(f)
    p = F/(2*(n-1))
    a = [round(10**((f[i]-p)/(n-2))) for i in range(n)]
    print(*a)
    return

#C
def C():
    s = S()
    n = len(s)
    g = [0]*n
    m = 26
    f = [set() for i in range(n)]
    f[ord(s[0])-ord("a")].add(0)
    for i in range(1,n):
        lis = set()
        k = ord(s[i])-ord("a")
        for j in range(k):
            lis |= f[j]
        for j in range(100):
            if j not in lis:
                g[i] = j
                break
        f[k].add(j)
    for i in g:
        if i == 0:
            print("Mike")
        else:
            print("Ann")
    return

#D
def D():
    n = I()
    b = LI()
    l = [i&-i for i in b]
    d = defaultdict(lambda : 0)
    for i in l:
        d[i] += 1
    m = [0,0]
    for i,j in list(d.items()):
        if m[1] < j:
            m = [i,j]
    ans = []
    for i in range(n):
        if m[0] != l[i]:
            ans.append(b[i])
    print(len(ans))
    print(*ans)
    return

#E
def E():

    return

#F
def F():

    return

#G
def G():

    return


#Solve
def __starting_point():
    D()

__starting_point()
