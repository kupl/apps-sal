(n, m, k, x, y) = list(map(int, input().split()))
t = m if n == 1 else n * m + (n - 2) * m
a = k // t
f = [[0] * 101 for _ in range(101)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        f[i][j] = a
        if i > 1 and i < n:
            f[i][j] += a
b = k % t
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if b == 0:
            break
        f[i][j] += 1
        b -= 1
    if b == 0:
        break
for i in range(n - 1, 1, -1):
    for j in range(1, m + 1):
        if b == 0:
            break
        f[i][j] += 1
        b -= 1
    if b == 0:
        break
maxnum = max(f[1][1], f[2][1], f[n - 1][1])
minnum = f[n][m]
sergei = f[x][y]
print(maxnum, minnum, sergei)
