INF = -float('inf')


def bellmanford(n, e, r):
    costs = [INF] * n
    costs[r] = 0
    for i in range(n):
        for u, v, c in e:
            if costs[u] + c > costs[v] and costs[u] != INF:
                costs[v] = costs[u] + c
                if i == n - 1 and v == n - 1:
                    return 'inf'
    return costs[n - 1]


n, m = list(map(int, input().split()))
edge = []
for i in range(m):
    a, b, t = list(map(int, input().split()))
    edge.append((a - 1, b - 1, t))

print((bellmanford(n, edge, 0)))
