def solve():
    from sys import stdin
    f_i = stdin
    inf = 5000001
    N = int(f_i.readline())
    P = map(int, f_i.readline().split())
    X = tuple(map(int, f_i.readline().split()))
    C = [[] for i in range(N)]
    for (c, p) in enumerate(P, start=1):
        C[p - 1].append(c)
    Y = [inf] * N

    def dfs(v):
        for c in C[v]:
            dfs(c)
        X_v = X[v]
        dp1 = [0] * (X_v + 1)
        dp2 = [inf] * (X_v + 1)
        for c in C[v]:
            X_c = X[c]
            Y_c = Y[c]
            for (i, b) in zip(range(X_c, X_v + 1), dp1):
                if b != inf:
                    dp2[i] = b + Y_c
            for (i, w, dp2_i) in zip(range(Y_c, X_v + 1), dp1, dp2[Y_c:]):
                tmp = w + X_c
                if tmp < dp2_i:
                    dp2[i] = tmp
            dp1 = dp2
            dp2 = [inf] * (X_v + 1)
        Y_v = min(dp1)
        Y[v] = Y_v
        return Y_v
    ans = dfs(0)
    if ans == inf:
        print('IMPOSSIBLE')
    else:
        print('POSSIBLE')


solve()
