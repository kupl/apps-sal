from scipy.sparse.csgraph import floyd_warshall
import numpy as np


def main():
    INF = 10**12
    N = int(input())
    A = [list(map(int, input().split(' '))) for _ in range(N)]
    wf = floyd_warshall(A)
    for i in range(N):
        A[i][i] = INF
        wf[i][i] = INF
    ans = 0
    for i in range(N):
        for j in range(N):
            if A[i][j] != wf[i][j]:
                print(-1)
                return
            if wf[i][j] < np.min(wf[i] + wf[j]):
                ans += wf[i][j]
    print(int(ans // 2))


def __starting_point():
    main()
__starting_point()
