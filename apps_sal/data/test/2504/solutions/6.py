"""
E - Travel by Car
https://atcoder.jp/contests/abc143/tasks/abc143_e

"""
import sys
from scipy.sparse.csgraph import floyd_warshall


def main(args):
    (N, M, L) = list(map(int, input().split()))
    g1 = [[float('inf')] * (N + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        g1[i][i] = 0
    for _ in range(M):
        (A, B, C) = list(map(int, input().split()))
        g1[A][B] = g1[B][A] = C
    d1 = floyd_warshall(g1)
    g2 = [[float('inf')] * (N + 1) for _ in range(N + 1)]
    for i in range(N + 1):
        for j in range(N + 1):
            if i == j:
                g2[i][j] = 0
            elif d1[i][j] <= L:
                g2[i][j] = g2[j][i] = 1
    d2 = floyd_warshall(g2)
    Q = int(input())
    for _ in range(Q):
        (s, t) = list(map(int, input().split()))
        print(-1 if d2[s][t] == float('inf') else int(d2[s][t]) - 1)


def __starting_point():
    main(sys.argv[1:])


__starting_point()
