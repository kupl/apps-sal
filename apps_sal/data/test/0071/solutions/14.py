(n, m, k, x1, y1) = map(int, input().split())
c = 0
if n == 1:
    mi = k // m
    ma = mi + 1 * int(k % m != 0)
    s = mi + 1 * int(k % m > y1 - 1)
else:
    c = k // (m * (2 * n - 2))
    d = k % (m * (2 * n - 2))
    q = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if 0 < i < n - 1:
                q[i][j] = 2 * c
            else:
                q[i][j] = c
    i = 0
    while d > 0:
        if i % (2 * n - 2) > n - 1:
            x = 2 * n - 2 - i % (2 * n - 2)
        else:
            x = i % (2 * n - 2)
        j = 0
        while d > 0 and j < m:
            q[x][j] += 1
            d -= 1
            j += 1
        i += 1
    ma = -1
    mi = 10 ** 100
    for i in range(n):
        for j in range(m):
            mi = min(q[i][j], mi)
            ma = max(q[i][j], ma)
    s = q[x1 - 1][y1 - 1]
print(ma, mi, s)
