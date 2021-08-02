n = int(input())
f = [[0] * (n + 1) for i in range(n + 1)]
g = [[0] * (n + 1) for i in range(n + 1)]
mod = 10**9 + 7
for i in range(1, n + 1):
    f[0][i] = g[0][i - 1]
    g[0][i] = f[0][i - 1] + 1
t = [0, 0]
for i in range(1, n + 1):
    for j in range(i, n + 1):
        if i > 0:
            f[i][j] += g[i - 1][j]
            t[0] = g[i - 1][j]
            t[1] = f[i - 1][j] + 1
        if j > i:
            f[i][j] += g[i][j - 1]
            t[0] += f[i][j - 1] + 1
            t[1] += g[i][j - 1]
        for k in t: g[i][j] = max(g[i][j], k)
print(g[n][n] % mod)
