(n, v) = list(map(int, input().split()))
g = [0 for x in range(3002)]
for i in range(n):
    (a, b) = list(map(int, input().split()))
    g[a] += b
r = 0
for i in range(1, 3002):
    c = v
    r += min(c, max(g[i - 1], 0))
    c -= max(g[i - 1], 0)
    if c > 0:
        r += min(c, g[i])
        g[i] = max(g[i] - c, 0)
print(r)
