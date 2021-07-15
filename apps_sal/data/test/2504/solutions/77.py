def main():
    from sys import stdin
    input=stdin.readline
    
    import numpy as np
    import scipy.sparse.csgraph as sp

    n, m, l = list(map(int, input().split()))
    abc = [list(map(int, input().split())) for _ in [0]*m]
    q = int(input())
    st = [list(map(int, input().split())) for _ in [0]*q]
    inf = 10**12
    dist = np.full((n, n), inf, dtype=np.int64)
    for i in range(n):
        dist[i][i] = 0
    for a, b, c in abc:
        dist[a-1][b-1] = c
        dist[b-1][a-1] = c
    dist = sp.shortest_path(dist)

    inf = 10**3
    dist2 = np.full((n, n), inf, dtype=np.int16)
    for i in range(n):
        for j in range(n):
            if dist[i][j] <= l:
                dist2[i][j] = 1
    dist2 = sp.shortest_path(dist2)

    for i in range(n):
        for j in range(n):
            if dist2[i][j] == inf:
                dist2[i][j] = -1
            else:
                dist2[i][j] -= 1
    for s, t in st:
        print((int(dist2[s-1][t-1])))


main()

