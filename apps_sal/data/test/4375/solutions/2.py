n, k = map(int, input().split())

a = list(map(int, input().split()))
g = [[] for i in range(n)]
for i in range(n - 1):
    v, u = map(int, input().split())
    v -= 1
    u -= 1
    g[v].append(u)
    g[u].append(v)

dp = [[] for i in range(n)]
d = [1 for i in range(n)]


def dfs(v, p=-1):
    dp[v].append(a[v])
    for u in g[v]:
        if u == p:
            continue
        dfs(u, v)
        tmp = [-10**18 for i in range(max(d[v], d[u] + 1))]
        for i in range(d[v]):
            for j in range(max(0, k - i), d[u]):
                tmp[min(i, j + 1)] = max(tmp[min(i, j + 1)], dp[v][i] + dp[u][j])
        for i in range(d[u]):
            tmp[i + 1] = max(tmp[i + 1], dp[u][i])
        for i in range(d[v]):
            dp[v][i] = max(dp[v][i], tmp[i])
        dp[v] += tmp[d[v]:]
        d[v] = max(d[v], d[u] + 1)
        for i in range(d[v] - 1, 0, -1):
            dp[v][i - 1] = max(dp[v][i - 1], dp[v][i])


dfs(0)
print(max(dp[0]))
