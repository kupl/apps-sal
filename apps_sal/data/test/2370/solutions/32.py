def main():
    n = int(input())
    if n == 1:
        print(0)
        return 0
    import numpy as np
    p = np.array([np.array(list(map(int, input().split()))) for _ in [0] * n])
    if n == 2:
        print(p[0][1])
        return 0
    import scipy.sparse.csgraph as sp
    ans = 0
    d = np.full((n, n), 0)
    for i in range(n):
        for j in range(i + 1, n):
            b = p[i][j]
            if b != np.sort(p[i] + p[j])[2]:
                d[i][j], d[j][i] = b, b
                ans += b
    s = sp.shortest_path(d)
    if (s == p).all():
        print(ans)
    else:
        print(-1)


main()
