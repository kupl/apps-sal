(n, m, Q) = map(int, input().split())
d = [[0 for i in range(n + 1)] for i in range(n + 1)]
for i in range(m):
    (l, r) = map(int, input().split())
    d[l][r] += 1
for i in range(n + 1):
    for j in range(n):
        d[i][j + 1] += d[i][j]
for i in range(n + 1):
    for j in range(n):
        d[n - 1 - j][i] += d[n - j][i]
for i in range(Q):
    (p, q) = map(int, input().split())
    print(d[p][q])
