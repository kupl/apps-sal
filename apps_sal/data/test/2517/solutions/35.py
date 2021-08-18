
from itertools import permutations
import numpy as np

HUGE = 10 ** 18


def main():
    n, m, r = list(map(int, input().split()))
    togo = list(map(int, input().split()))
    adj_mat = [[HUGE for j in range(n)] for i in range(n)]
    for i in range(n):
        adj_mat[i][i] = HUGE
    for i in range(m):
        a, b, c = list(map(int, input().split()))
        a0 = a - 1
        b0 = b - 1
        adj_mat[a0][b0] = c
        adj_mat[b0][a0] = c
    adj_mat = np.array(adj_mat)

    wf(adj_mat, n)

    res = HUGE
    for way in permutations(togo):
        assert len(way) > 1
        x = 0
        for i in range(len(way) - 1):
            x += adj_mat[way[i] - 1][way[i + 1] - 1]
        res = min(res, x)

    print(res)


def wf(adj_mat, n):
    for k in range(n):
        for i in range(n):
            adj_mat[i, :] = np.minimum(adj_mat[i, :], adj_mat[i][k] + adj_mat[k, :])


def __starting_point():
    main()


__starting_point()
