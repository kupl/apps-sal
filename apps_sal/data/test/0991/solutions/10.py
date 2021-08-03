import heapq
N, M, init_silver = map(int, input().split())
MAX_COST = 2500
init_silver = min(init_silver, MAX_COST)

G = [[] for _ in range(N)]
for i in range(M):
    u, v, silver_cost, time_cost = map(int, input().split())
    u, v = u - 1, v - 1
    G[u].append([v, silver_cost, time_cost])
    G[v].append([u, silver_cost, time_cost])

change_rate, change_cost = [], []
for i in range(N):
    rate, cost = map(int, input().split())
    G[i].append([i, -rate, cost])
    change_rate.append(rate)
    change_cost.append(cost)


# dp[i][silver] := 頂点iにいて銀貨をsilver枚持っているような状況を作るために必要な最小時間
dp = [[float('inf')] * (MAX_COST + 1) for _ in range(N)]
dp[0][init_silver] = 0

# 優先度付きキュー: (time, node, silver)
hq = [(0, 0, init_silver)]
while hq:
    time, node, silver = heapq.heappop(hq)

    # self_loop_silver = min(silver + change_rate[node], MAX_COST)
    # self_loop_cost = time + change_cost[node]
    # if self_loop_cost < dp[node][self_loop_silver]:
    #     dp[node][self_loop_silver] = self_loop_cost
    #     heapq.heappush(hq, (time + change_cost[node], node, self_loop_silver))

    for to, silver_cost, time_cost in G[node]:
        remain_silver = min(silver - silver_cost, MAX_COST)
        if remain_silver < 0:
            continue

        dp_next_value = time + time_cost
        if dp[to][remain_silver] <= dp_next_value:
            continue

        dp[to][remain_silver] = dp_next_value
        heapq.heappush(hq, (dp_next_value, to, remain_silver))

print(*[min(d) for d in dp[1:]], sep="\n")
