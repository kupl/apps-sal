n, m = map(int, input().split())
#g=[[]for _ in range(n)]
abc = [list(map(int, input().split())) for _ in range(m)]
abc = [[a - 1, b - 1, -c] for a, b, c in abc]
# BellmanFord
# ベルマンフォード法


def BellmanFord(edges, num_v, source):
    # グラフの初期化
    inf = float("inf")
    dist = [inf for i in range(num_v)]
    dist[source] = 0
    # 辺の緩和
    for i in range(num_v):
        for edge in edges:
            if dist[edge[0]] != inf and dist[edge[1]] > dist[edge[0]] + edge[2]:
                dist[edge[1]] = dist[edge[0]] + edge[2]
                # if i==num_v-1: return -1
    negative = [False] * n
    for i in range(num_v):
        for edge in edges:
            if negative[edge[0]]:
                negative[edge[1]] = True
            if dist[edge[0]] != inf and dist[edge[1]] > dist[edge[0]] + edge[2]:
                negative[edge[1]] = True
    return dist[n - 1], negative[n - 1]


c, d = BellmanFord(abc, n, 0)
# 負の閉路にNが含まれない時はinfじゃない
if d:
    print('inf')
else:
    print(-c)
