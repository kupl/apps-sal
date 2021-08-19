INF = 1000
n = int(input())
desc = list(map(int, input().split()))
r = {}
g = {}
c = {}
r[0] = 0
g[0] = 0
c[0] = 0
i = 0
for x in desc:
    i += 1
    if x == 0:
        g[i] = INF
        c[i] = INF
        r[i] = 1 + min([g[i - 1], r[i - 1], c[i - 1]])
    elif x == 1:
        g[i] = INF
        c[i] = min(r[i - 1], g[i - 1])
        r[i] = 1 + min([g[i - 1], r[i - 1], c[i - 1]])
    elif x == 2:
        g[i] = min(r[i - 1], c[i - 1])
        c[i] = INF
        r[i] = 1 + min([g[i - 1], r[i - 1], c[i - 1]])
    elif x == 3:
        r[i] = 1 + min([g[i - 1], r[i - 1], c[i - 1]])
        g[i] = min(r[i - 1], c[i - 1])
        c[i] = min(r[i - 1], g[i - 1])
print(min([r[n], g[n], c[n]]))
