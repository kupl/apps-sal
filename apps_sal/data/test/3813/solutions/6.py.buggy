n = int(input())
p = list(map(int, input().split()))
x = list(map(int, input().split()))
g = [[] for i in range(n)]
for i in range(n - 1):
    g[p[i] - 1].append(i + 1)
kyo = [float("inf")] * n


def dfs(x, y):
    kyo[x] = y
    for i in g[x]:
        dfs(i, y + 1)


dfs(0, 0)
hukai = []
for i in range(n):
    hukai.append([kyo[i], i])
hukai.sort(key=lambda x: -x[0])
INF = float("inf")
dp = [0] * n
for j, i in hukai:
    if len(g[i]) == 0:
        continue
    tmp = []
    MIN = 0
    MAX = 0
    for k in g[i]:
        tmp.append([dp[k], x[k]])
        MIN += min(dp[k], x[k])
        MAX += max(dp[k], x[k])
    d = {}
    d[MAX] = MIN
    for k in tmp:
        MIN = min(k)
        MAX = max(k)
        co = list(d.keys())
        co.sort(key=lambda x: -x)
        for l in co:
            d[l - MAX + MIN] = min(d.get(l - MAX + MIN, INF), d[l] - MIN + MAX)
    co = list(d.keys())
    co.sort()
    for l in co:
        if d[l] <= x[i]:
            dp[i] = l
            break
    else:
        print("IMPOSSIBLE")
        return
print("POSSIBLE")
