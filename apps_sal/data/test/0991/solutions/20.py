from heapq import heappush, heappop

infi = 10 ** 20
n, m, s = map(int, input().split())

s = min(s, n * 50)

edges = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, a, b = map(int, input().split())
    edges[v].append((u, a, b))
    edges[u].append((v, a, b))

exchange = [(0, 0)] * (n + 1)

for edge_num in range(1, n + 1):
    c, d = map(int, input().split())
    exchange[edge_num] = (c, d)

start = 1
dp = [[infi] * (n * 50 + 1) for _ in range(n + 1)]


def dijkstra(edges, start, s, dp):
    dp[start][s] = 0
    edgelist = []
    heappush(edgelist, (0, s, start))
    while edgelist:
        nowtime, nowmoney, nowedge = heappop(edgelist)
        if dp[nowedge][nowmoney] != nowtime:
            continue
        deltamoney, deltatime = exchange[nowedge]
        nextmoney = min(nowmoney + deltamoney, n * 50)
        nexttime = nowtime + deltatime
        if dp[nowedge][nextmoney] > nexttime:
            dp[nowedge][nextmoney] = nexttime
            heappush(edgelist, (nexttime, nextmoney, nowedge))
        for v, vmoney, vtime in edges[nowedge]:
            nexttime = nowtime + vtime
            nextmoney = nowmoney - vmoney
            if nextmoney < 0:
                continue
            if dp[v][nextmoney] > nexttime:
                dp[v][nextmoney] = nexttime
                heappush(edgelist, (nexttime, nextmoney, v))
    return dp


time = dijkstra(edges, start, s, dp)

ans = [infi] * (n + 1)
for i in range(1, n + 1):
    for j in range(n * 50 + 1):
        ans[i] = min(ans[i], dp[i][j])

print(*ans[2: (n + 1)], sep="\n")
