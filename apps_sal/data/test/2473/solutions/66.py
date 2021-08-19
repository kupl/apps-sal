import sys
from bisect import bisect_left
from itertools import accumulate
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    (N, K, *XY) = list(map(int, read().split()))
    X = set()
    Y = set()
    for (i, (x, y)) in enumerate(zip(*[iter(XY)] * 2)):
        X.add(x - 1)
        Y.add(y - 1)
    X = sorted(X)
    Y = sorted(Y)
    (P, Q) = (len(X), len(Y))
    G = [[0] * Q for _ in range(P)]
    for (x, y) in zip(*[iter(XY)] * 2):
        G[bisect_left(X, x - 1)][bisect_left(Y, y - 1)] = 1
    csum = [[0] * (Q + 1) for _ in range(P + 1)]
    for i in range(P):
        for j in range(Q):
            csum[i + 1][j + 1] = csum[i + 1][j] + csum[i][j + 1] - csum[i][j] + G[i][j]
    ans = -1
    for x1 in range(P):
        for x2 in range(x1, P + 1):
            for y1 in range(Q):
                for y2 in range(y1, Q + 1):
                    if csum[x2][y2] - csum[x1][y2] - csum[x2][y1] + csum[x1][y1] >= K:
                        if ans > (X[x2 - 1] - X[x1]) * (Y[y2 - 1] - Y[y1]) or ans == -1:
                            ans = (X[x2 - 1] - X[x1]) * (Y[y2 - 1] - Y[y1])
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
