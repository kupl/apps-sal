import sys
import numpy as np
from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall, shortest_path
input = sys.stdin.readline


def main():
    (n, m, l) = map(int, input().split())
    wf = [[0 for i in range(n)] for j in range(n)]
    for _ in range(m):
        (a, b, c) = map(int, input().split())
        wf[a - 1][b - 1] = wf[b - 1][a - 1] = c
    wf = np.array(wf)
    for i in range(n):
        wf[i][i] = 0
    wf = shortest_path(wf, method='FW')
    for i in range(n):
        for j in range(n):
            if wf[i][j] <= l:
                wf[i][j] = 1
            else:
                wf[i][j] = 301
    wf = shortest_path(wf, method='FW')
    q = int(input())
    ans = [None] * q
    for i in range(q):
        (s, t) = map(int, input().split())
        if wf[s - 1][t - 1] < 301:
            ans[i] = int(wf[s - 1][t - 1])
        else:
            ans[i] = 0
    for i in range(q):
        print(ans[i] - 1)


def __starting_point():
    main()


__starting_point()
