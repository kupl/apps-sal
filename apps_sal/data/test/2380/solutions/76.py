import sys, math
from functools import lru_cache
import datetime
sys.setrecursionlimit(500000)
MOD = 10**9+7

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]


def main():
    N, M = mi()
    A = list(mi())
    A.sort()
    BC = [list(mi()) for i in range(M)]
    BC.sort(reverse=True, key=lambda x: x[1])

    D = []

    for i in range(M):
        for j in range(BC[i][0]):
            D.append(BC[i][1])
            if len(D) == N:
                break
        if len(D) == N:
            break

    while len(D) < N:
        D.append(0)

    print(sum(max(A[i], D[i]) for i in range(N)))


def __starting_point():
    main()
__starting_point()
