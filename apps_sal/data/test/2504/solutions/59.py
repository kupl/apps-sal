from math import isinf
from scipy.sparse.csgraph import shortest_path
from scipy.sparse import csr_matrix

INF = float('inf')


def main():
    N, M, L = list(map(int, input().split()))
    E = [[INF] * N for _ in range(N)]
    for _ in range(M):
        a, b, c = list(map(int, input().split()))
        E[a - 1][b - 1] = c
        E[b - 1][a - 1] = c
    EE = shortest_path(csr_matrix(E))
    E = [[1 if EE[i][j] <= L else INF for j in range(N)] for i in range(N)]
    EE = shortest_path(csr_matrix(E))
    Q = int(input())
    for _ in range(Q):
        s, t = list(map(int, input().split()))
        x = EE[s - 1][t - 1]
        print((-1 if isinf(x) else int(x) - 1))


main()
