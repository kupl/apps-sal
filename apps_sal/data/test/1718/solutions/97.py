import sys
sys.setrecursionlimit(10 ** 6)
def II(): return int(sys.stdin.readline())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LC(): return list(input())
def IC(): return [int(c) for c in input()]
def MI(): return map(int, input().split())


def solve():
    N, K = MI()
    A = LI()
    One = A.index(1)
    from math import ceil, floor
    if(N == K):
        print(1)
        return
    else:
        print(ceil((N - K) / (K - 1)) + 1)
    return


solve()
