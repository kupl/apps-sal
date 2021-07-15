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
    leftA = [x for x in A[:N]]
    heapq.heapify(leftA)
    subsum = sum(leftA)
    Aleftsum[wakeme] = subsum
    for i in range(N):
        heapq.heappush(leftA, A[wakeme + i])
        subsum += A[wakeme + i]
        subsum -= heapq.heappop(leftA)
        Aleftsum[wakeme+i+1] = subsum

    Arightsum = [0 for _ in range(3*N+1)]
    rightA = [-x for x in A[-N:]]
    heapq.heapify(rightA)
    subsum = sum(rightA)
    wakeme = 2*N
    Arightsum[wakeme] = -subsum
    for i in range(1, N+1):
        heapq.heappush(rightA, -A[wakeme-i])
        subsum -= A[wakeme - i]
        subsum -= heapq.heappop(rightA)
        Arightsum[wakeme - i] = -subsum
    ans = -inf
    for i in range(N, 2*N+1):
        ans = max(ans, Aleftsum[i] - Arightsum[i])
    print(ans)
main()


