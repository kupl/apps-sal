def main():
    from sys import stdin
    input = stdin.readline
    n, m, r = list(map(int, input().split()))
    root = list(map(int, input().split()))
    abc = [list(map(int, input().split())) for _ in [0]*m]

    import numpy as np
    import scipy.sparse.csgraph as sp
    inf = float('inf')
    d = np.full((n, n), inf)
    for i in range(n):
        d[i][i] = 0
    for a, b, c in abc:
        d[a-1][b-1] = c
        d[b-1][a-1] = c
    # indices=xでxからの単一始点に,return_predecessors=Trueで経路が出る
    s = sp.shortest_path(d)

    from itertools import permutations

    p = list(permutations(root))

    D = 10**10
    for i in p:
        d = 0
        for j in range(len(i)-1):
            d += s[i[j]-1][i[j+1]-1]
        D = min(D, d)
    print((int(D)))


main()

