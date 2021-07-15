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
    N = I()
    A = LI()
    wakeme = N
    Aleftsum = [0 for _ in range(3*N+1)]
    Arightsum = [0 for _ in range(3*N+1)]

    leftA = [x for x in A[:N]]
    rightA = [-x for x in A[-N:]]

    heapq.heapify(leftA)
    heapq.heapify(rightA)

    lsum = sum(leftA)
    rsum = sum(rightA)

    Aleftsum[wakeme] = lsum
    Arightsum[2*N] = -rsum

    # [0, N)から[0, 2N)までの和が欲しい
    # Aleftsum(i): [0, i)までの上位N個の和

    # [2N, 3N)から[N, 3N)までの和が欲しい
    # Arightsum(i): [i, 3N)までの上位N個の和

    for i in range(N):
        # [0, N+1)から[0, 2N)までやる。
        # [0, wakeme + i + 1)の和を計算する。
        # wakeme=Nなので、wakeme + i + 1 = 2N -> i = N - 1
        newl = A[wakeme + i]
        lsum += newl
        lsum -= heapq.heappushpop(leftA, newl)
        Aleftsum[wakeme+i+1] = lsum

        # [2N-1, 3N)から[N, 3N)までやる。
        # r_wakeme = 2N-1として、
        # r_wakeme - i = 2N - 1 -> i=0
        # r_wakeme - i = N -> i=N-1
        newr = A[2*N-1 - i]
        rsum -= newr
        rsum -= heapq.heappushpop(rightA, -newr)
        Arightsum[2*N-1 - i] = -rsum

    ans = -inf
    for i in range(N, 2*N+1):
        ans = max(ans, Aleftsum[i] - Arightsum[i])

    print(ans)
main()


