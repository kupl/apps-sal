import heapq


n, m, s = map(int, input().split())
if s >= 2500:
    s = 2499

edges = [[] for _ in range(n)]
for _ in range(m):
    from_, to, cost, time = map(int, input().split())
    edges[from_ - 1].append((to - 1, cost, time))
    edges[to - 1].append((from_ - 1, cost, time))

banks = []
for i in range(n):
    coin, time = map(int, input().split())
    banks.append((coin, time))

INF = float('INF')
DP = [[INF] * 2500 for _ in range(n)]
ans = [INF] * n


def push_todo(node, coin, time):
    if coin < 0:
        return
    if time >= DP[node][coin]:
        return
    heapq.heappush(todo, (time, node, coin))


def charge(node, current_coin, current_time):
    coin, time = banks[node]
    new_coin = current_coin + coin
    if new_coin >= 2500:
        new_coin = 2499
    push_todo(node, new_coin, current_time + time)


todo = [(0, 0, s)]
while todo:
    current_time, node, current_coin = heapq.heappop(todo)
    if current_time >= DP[node][current_coin]:
        continue

    if current_time < ans[node]:
        ans[node] = current_time

    DP[node][current_coin] = current_time
    charge(node, current_coin, current_time)

    for to, cost, time in edges[node]:
        push_todo(to, current_coin - cost, current_time + time)

for a in ans[1:]:
    print(a)
