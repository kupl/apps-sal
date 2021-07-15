import sys
sys.setrecursionlimit(10 ** 8)

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    N, M, Q = ZZ()
    lr = sorted([ZZ() for _ in range(M)])
    query = [ZZ() for _ in range(Q)]
    p = [[0] * (N+1) for _ in range(N+1)]
    for l, r in lr: p[l][r] += 1
    for i in range(1, N+1)[::-1]:
        for j in range(1, N+1):
            if j+1 <= N: p[i][j+1] += p[i][j]
            if 0 <= i-1: p[i-1][j] += p[i][j]
            if j+1 <= N and 0 <= i-1: p[i-1][j+1] -= p[i][j]
    for a, b in query: print((p[a][b]))

    return

def __starting_point():
    main()

__starting_point()
