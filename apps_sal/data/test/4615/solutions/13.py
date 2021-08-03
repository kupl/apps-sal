a, b, c, d, e, f = map(int, input().split())
g = [-1] * 9999
g[a * 100] = 0
g[b * 100] = 0
h = [a * 100, 0]
p = 0
for i in range(1, f + 1):
    if g[i] == -1:
        continue
    if (g[i] + c) / (i - g[i]) <= e * 0.01:
        g[i + c] = max(g[i] + c, g[i + c])
    if (g[i] + d) / (i - g[i]) <= e * 0.01:
        g[i + d] = max(g[i] + d, g[i + d])
    g[i + a * 100] = max(g[i + a * 100], g[i])
    g[i + b * 100] = max(g[i + b * 100], g[i])
    if g[i] / i > p:
        p = g[i] / i
        h = [i, g[i]]
print(*h)
