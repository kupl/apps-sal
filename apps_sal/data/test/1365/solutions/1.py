n, m = map(int, input().split())

edge_to = [0 for i in range(n * 2 + 1)]
edge_next = [0 for i in range(n * 2 + 1)]
son = [0 for i in range(n + 1)]


def add_edge(u, v):
    nonlocal edge_next, edge_to, son, tot
    tot += 1
    edge_to[tot] = v
    edge_next[tot] = son[u]
    son[u] = tot


tot = 0
MOD = 10**9 + 7
dp = [[0] * (m * 2 + 2) for i in range(n + 1)]


def dp_tree(x, fa):
    nonlocal edge_next, edge_to, m, son, dp
    dp[x][0] = 1
    dp[x][m + 1] = 1
    f = [0 for i in range(m * 2 + 2)]
    i = son[x]
    while (i):
        f = [0 for w in range(m * 2 + 2)]
        to = edge_to[i]
        i = edge_next[i]
        if (to == fa):
            continue
        dp_tree(to, x)
        for j in range(2 * m + 2):
            for k in range(2 * m + 1):
                if (j + k <= 2 * m):
                    f[min(j, k + 1)] += (dp[x][j] * dp[to][k]) % MOD
                    f[min(j, k + 1)] %= MOD
                else:
                    f[max(j, k + 1)] += (dp[x][j] * dp[to][k]) % MOD
                    f[max(j, k + 1)] %= MOD
        dp[x] = f


for i in range(n - 1):
    u, v = map(int, input().split())
    add_edge(u, v)
    add_edge(v, u)

dp_tree(1, -1)
res = 0
for i in range(m + 1):
    res += dp[1][i]
    res %= MOD
print(res)
