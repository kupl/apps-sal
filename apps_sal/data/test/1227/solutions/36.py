import sys
import numpy as np


def input():
    return sys.stdin.readline().rstrip()


N = list(map(int, input()))
K = int(input())


def solve():
    dp_sm = np.zeros((len(N), K + 1), np.int64)
    dp_lg = np.zeros((len(N), K + 1), np.int64)
    dp_sm[0][0] = 1
    dp_sm[0][1] = N[0] - 1
    dp_lg[0][0] = 0
    dp_lg[0][1] = 1
    for i in range(len(N) - 1):
        for j in range(K + 1):
            dp_sm[i + 1][j] += dp_sm[i][j]
            if N[i + 1] != 0:
                dp_sm[i + 1][j] += dp_lg[i][j]
            if j < K:
                dp_sm[i + 1][j + 1] += dp_sm[i][j] * 9
            if j < K and N[i + 1] != 0:
                dp_sm[i + 1][j + 1] += dp_lg[i][j] * (N[i + 1] - 1)
                dp_lg[i + 1][j + 1] += dp_lg[i][j]
            if N[i + 1] == 0:
                dp_lg[i + 1][j] += dp_lg[i][j]
    print(dp_sm[len(N) - 1][K] + dp_lg[len(N) - 1][K])


def __starting_point():
    solve()


__starting_point()
