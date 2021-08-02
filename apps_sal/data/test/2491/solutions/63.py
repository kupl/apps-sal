N, M = map(int, input().split())
INF = float("inf")

start = []
end = []
weight = []
node_cost = [-INF] * N
for _ in range(M):
    a, b, c = map(int, input().split())
    start.append(a - 1)
    end.append(b - 1)
    weight.append(c)

node_cost[0] = 0
for _ in range(N - 1):
    for i in range(M):
        new_cost = node_cost[start[i]] + weight[i]
        if new_cost > node_cost[end[i]]:
            node_cost[end[i]] = new_cost
ans = node_cost[N - 1]
cycle = [False] * N
for _ in range(N):
    for i in range(M):
        if cycle[start[i]]:
            cycle[end[i]] = True
        new_cost = node_cost[start[i]] + weight[i]
        if new_cost > node_cost[end[i]]:
            cycle[end[i]] = True
if cycle[N - 1]:
    ans = "inf"
print(ans)
