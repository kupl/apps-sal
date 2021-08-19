# snuke解説板
from heapq import heappush, heappop

infi = 10 ** 20
n, m, s = map(int, input().split())

s = min(s, n * 50)

edges = [[] for _ in range(n + 1)]
# edge:1-50, max silver=0-2500

for _ in range(m):  # a円, b分
    u, v, a, b = map(int, input().split())
    edges[v].append((u, a, b))
    edges[u].append((v, a, b))

exchange = [(0, 0)] * (n + 1)

for edge_num in range(1, n + 1):  # c円, d分
    c, d = map(int, input().split())
    exchange[edge_num] = (c, d)

start = 1
# dp[i][j], 頂点iにお金jを持って到達する最低時間→時間に関してDAG
dp = [[infi] * (n * 50 + 1) for _ in range(n + 1)]


def dijkstra(edges, start, s, dp):
    dp[start][s] = 0
    edgelist = []
    heappush(edgelist, (0, s, start))  # 時間, お金, 頂点
    while edgelist:
        nowtime, nowmoney, nowedge = heappop(edgelist)
        # 遷移させる条件はedge,moneyの組み合わせに対してその時の最小値が出てきたときのみ→最小値以外は飛ばす。
        if dp[nowedge][nowmoney] != nowtime:
            continue
        # 両替
        deltamoney, deltatime = exchange[nowedge]
        nextmoney = min(nowmoney + deltamoney, n * 50)
        nexttime = nowtime + deltatime
        if dp[nowedge][nextmoney] > nexttime:
            dp[nowedge][nextmoney] = nexttime
            heappush(edgelist, (nexttime, nextmoney, nowedge))
        # 移動
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
