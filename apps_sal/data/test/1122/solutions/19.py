import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools
from collections import deque

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

DR = [1, -1, 0, 0]
DC = [0, 0, 1, -1]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
     
def main():
    N, M = LI()
    used = [0 for _ in range(N)]
    cur = 0
    pairs = []
    used = set()
    if N % 2 == 0:
        a = 1
        b = N
        while len(pairs) < M:
            if b-a in used or N + a -b in used or b - a == N//2:
                b -= 1
            pairs.append((a, b))
            used.add(b-a)
            used.add(N+a - b)
            a += 1
            b -= 1

    else:
        a = 1
        b = N - 1
        while len(pairs) < M:
            pairs.append((a, b))
            a += 1
            b -= 1
    for p in pairs:
        print((p[0], p[1]))



main()


