import sys
from itertools import permutations


def input():
    return sys.stdin.readline().strip()


def main():
    N, M, R = list(map(int, input().split()))

    def warshall_floyd(d):
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    tmp = d[i][k] + d[k][j]
                    if d[i][j] > tmp:
                        d[i][j] = tmp
        return d

    r = list(map(int, input().split()))
    d = [[float("inf")] * N for i in range(N)]
    for i in range(M):
        x, y, z = list(map(int, input().split()))
        d[x - 1][y - 1] = z
        d[y - 1][x - 1] = z
    for i in range(N):
        d[i][i] = 0
    D = warshall_floyd(d)
    P = list(permutations(r))
    cost = float("inf")
    for p in P:
        c = 0
        for i in range(R - 1):
            c += D[p[i] - 1][p[i + 1] - 1]
        if c < cost:
            cost = c
    print(cost)


def __starting_point():
    main()


__starting_point()
