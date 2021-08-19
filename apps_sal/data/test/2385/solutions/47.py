import sys
input = sys.stdin.readline


def main():
    n = int(input())
    g = [[] for _ in range(n)]
    for i in range(n - 1):
        (a, b) = map(int, input().split())
        (a, b) = (a - 1, b - 1)
        g[a].append(b)
        g[b].append(a)
    mod = 10 ** 9 + 7
    N = 10 ** 6
    g1 = [1, 1]
    g2 = [1, 1]
    inverse = [0, 1]
    for i in range(2, N + 1):
        g1.append(g1[-1] * i % mod)
        inverse.append(-inverse[mod % i] * (mod // i) % mod)
        g2.append(g2[-1] * inverse[-1] % mod)
    s = []
    s.append(0)
    parent = [-1] * n
    order = []
    while s:
        v = s.pop()
        order.append(v)
        for u in g[v]:
            if u == parent[v]:
                continue
            parent[u] = v
            s.append(u)
    dp = [1] * n
    c = [0] * n
    order.reverse()
    for v in order:
        dp[v] *= g1[c[v]]
        dp[v] %= mod
        c[v] += 1
        if parent[v] == -1:
            continue
        c[parent[v]] += c[v]
        dp[parent[v]] *= dp[v] * g2[c[v]]
        dp[parent[v]] %= mod
    order.reverse()
    ans = [0] * n
    for v in order:
        ans[v] = dp[v]
        for u in g[v]:
            if u == parent[v]:
                continue
            dp[u] *= ans[v] * g2[c[v] - 1] * g1[c[v] - 1 - c[u]] * g1[c[u]] * pow(dp[u], mod - 2, mod)
            dp[u] *= g2[c[u] - 1]
            dp[u] *= g1[c[v] - 1]
            dp[u] *= g2[c[v] - c[u]]
            dp[u] %= mod
            c[u] = c[v]
    for i in range(n):
        print(ans[i] % mod)


def __starting_point():
    main()


__starting_point()
