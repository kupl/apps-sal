n, m, s = list(map(int, input().split()))

edges = [[] for _ in range(n)]
for _ in range(m):
    u, v, a, b = list(map(int, input().split()))
    u, v = u-1, v-1
    edges[u].append((v, a, b))
    edges[v].append((u, a, b))

banks = tuple(tuple(map(int, input().split())) for _ in range(n))

max_s = 50 * (n-1)

s = min(s, max_s)

import heapq

h = []
dp = [[float('inf')] * (max_s+1) for _ in range(n)]
ans = [float('inf')] * n

heapq.heappush(h, (0, 0, s))
while h:
    time, node, coin = heapq.heappop(h)
    if time >= dp[node][coin]:
        continue
    dp[node][coin] = time
    if time < ans[node]:
        ans[node] = time

    c, d = banks[node]
    if coin < max_s:
        heapq.heappush(h, (time+d, node, min(coin + c, max_s)))

    for n, a, b in edges[node]:
        new_time = time + b
        new_coin = coin - a
        if new_coin < 0 or new_time >= dp[n][new_coin]:
            continue
        heapq.heappush(h, (new_time, n, new_coin))

for a in ans[1:]:
    print(a)

