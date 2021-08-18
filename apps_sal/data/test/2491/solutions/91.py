INF = float("inf")


def Bellmanford(n, edges):
    dp = [INF] * n
    dp[0] = 0

    for i in range(n):
        for u, v, c in edges:
            if dp[u] != INF and dp[u] + c < dp[v]:
                dp[v] = dp[u] + c
                if i == n - 1 and v == n - 1:
                    return "inf"

    return -dp[n - 1]


N, M = map(int, input().split())
E = []

for i in range(M):
    a, b, c = map(int, input().split())
    E.append((a - 1, b - 1, -c))

ans = Bellmanford(N, E)

print(ans)
