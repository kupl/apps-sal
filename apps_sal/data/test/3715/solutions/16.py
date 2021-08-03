INF = 1000
n = int(input())
desc = list(map(int, input().split()))
r, g, c = {}, {}, {}
r[0], g[0], c[0], i = 0, 0, 0, 0
for x in desc:
    i += 1
    r[i] = 1 + min([g[i - 1], r[i - 1], c[i - 1]])
    g[i] = INF if x < 2 else min(r[i - 1], c[i - 1])
    c[i] = INF if x % 2 == 0 else min(r[i - 1], g[i - 1])
print(min([r[n], g[n], c[n]]))
