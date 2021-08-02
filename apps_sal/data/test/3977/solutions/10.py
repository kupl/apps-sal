n, m, k = list(map(int, input().split()))
C = list(map(int, input().split()))
g = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = list(map(int, input().split()))
    g[a][b] = g[b][a] = 1

y = [0] * k
v = [0] * (n + 1)


def dfs(c, x):
    y[c] += 1
    v[x] = 1
    for j in range(n + 1):
        if g[x][j] == 1 and v[j] == 0:
            dfs(c, j)


for c in range(k):
    v = [0] * (n + 1)
    dfs(c, C[c])
s = n - sum(y)
mm = max(y)
for i in range(k):
    if y[i] == mm:
        y[i] += s
        break

y = list([w * (w - 1) // 2 for w in y])
print(sum(y) - m)
