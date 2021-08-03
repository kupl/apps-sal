import numpy as np
from scipy.sparse.csgraph import floyd_warshall
import itertools


def main():
    N, M, R = list(map(int, input().split(' ')))
    towns = list(map(lambda t: int(t) - 1, input().split(' ')))
    A = np.zeros((N, N), dtype=int)
    for _ in range(M):
        a, b, c = list(map(int, input().split(' ')))
        A[a - 1][b - 1] = c
        A[b - 1][a - 1] = c
    fw = floyd_warshall(A)
    d = fw[towns, :][:, towns]
    min_d = 10**12
    for trip in itertools.permutations(range(R)):
        min_d = min([min_d, sum([d[trip[i]][trip[i + 1]] for i in range(len(trip) - 1)])])
    print(int(min_d))


def __starting_point():
    main()


__starting_point()
