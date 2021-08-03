from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall
import numpy as np
import sys
input = sys.stdin.readline


def main():
    n, m, l = map(int, input().split())
    F = np.zeros((n, n))
    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        F[a, b] = c
        F[b, a] = c
    csr = csr_matrix(F)
    A = floyd_warshall(csr)
    G = np.zeros((n, n))
    for i in range(n - 1):
        for j in range(i + 1, n):
            if A[i][j] <= l:
                G[i, j] = 1
                G[j, i] = 1
    ncsr = csr_matrix(G)
    B = floyd_warshall(ncsr)
    q = int(input())
    for _ in range(q):
        s, t = map(int, input().split())
        k = B[s - 1][t - 1]
        if k == float("inf"):
            print(-1)
        else:
            print(int(k) - 1)


def __starting_point():
    main()


__starting_point()
