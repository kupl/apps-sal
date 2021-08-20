def resolve():
    (n, m, q) = map(int, input().split())
    rosen = [[0] * n for _ in range(n)]
    for i in range(m):
        (l, r) = map(int, input().split())
        l -= 1
        r -= 1
        rosen[l][r] += 1
    cum = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        if i == 0:
            cum[0][0] = rosen[0][0]
            for j in range(1, n):
                cum[0][j] = cum[0][j - 1] + rosen[0][j]
        else:
            cum[i][0] = cum[i - 1][0] + rosen[i][0]
            for j in range(1, n):
                cum[i][j] = cum[i - 1][j] + cum[i][j - 1] - cum[i - 1][j - 1] + rosen[i][j]
    for i in range(q):
        (p, q) = map(int, input().split())
        p -= 1
        q -= 1
        if p == 0:
            print(cum[q][q])
        else:
            print(cum[q][q] - cum[p - 1][q] - cum[q][p - 1] + cum[p - 1][p - 1])


resolve()
