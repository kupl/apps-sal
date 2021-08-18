import heapq

N, M, S = list(map(int, input().rstrip().split()))
UVAB_list = [list(map(int, input().rstrip().split())) for i in range(M)]
CD_list = [list(map(int, input().rstrip().split())) for i in range(N)]

max_money = 2500
S = min(max_money, S)

graph = [None] + [[] for _ in range(N)]

change = [None] + [() for _ in range(N)]

dp = [None] + [[float("inf")] * (max_money + 1) for _ in range(N)]
dp[1][S] = 0


for u, v, a, b in UVAB_list:
    graph[u].append((v, a, b))
    graph[v].append((u, a, b))

for i, (c, d) in enumerate(CD_list):
    change[i + 1] = (c, d)

heap = [(0, 1, S)]


while heap:
    cur_time, cur_city, cur_mone = heapq.heappop(heap)

    changed_money = cur_mone + change[cur_city][0]
    changed_time = cur_time + change[cur_city][1]

    if (changed_money <= max_money) and (changed_time < dp[cur_city][changed_money]):
        dp[cur_city][changed_money] = changed_time
        heapq.heappush(heap, (changed_time, cur_city, changed_money))

    for next_city, cost_coin, cost_time in graph[cur_city]:
        next_time = cur_time + cost_time
        next_money = min(max_money, cur_mone - cost_coin)

        if (cur_mone >= cost_coin) and (next_time < dp[next_city][next_money]):
            dp[next_city][next_money] = next_time
            heapq.heappush(heap, (next_time, next_city, next_money))


for row in dp[2:]:
    print((min(row)))
