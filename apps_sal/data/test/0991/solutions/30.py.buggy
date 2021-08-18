import heapq
import sys
input = sys.stdin.readline

INF = 10 ** 18


class Edge():
    def __init__(self, end, cost, time):
        self.end = end
        self.cost = cost
        self.time = time


dp = []
h = []


def push(t, v, x):
    if x < 0:
        return
    if dp[v][x] <= t:
        return
    dp[v][x] = t
    heapq.heappush(h, (t, v, x))


def dijkstra(n, G, cd, start, s, max_s):
    nonlocal dp
    dp = [[INF for j in range(max_s + 1)] for i in range(n)]
    push(0, start, s)

    while h:
        # 使っていない頂点のうち、現時点で最も到達短時間が短いものを選びvとする
        t, v, x = heapq.heappop(h)
        if dp[v][x] < t:
            continue
        # 両替
        if x < max_s:
            push(t + cd[v][1], v, min(x + cd[v][0], max_s))
        # vから到達可能な頂点について、到達時間が短くなれば更新
        for e in G[v]:
            push(t + e.time, e.end, x - e.cost)


n, m, s = map(int, input().split())
uvab = [list(map(int, input().split())) for _ in range(m)]
cd = [list(map(int, input().split())) for _ in range(n)]

es = [[] for i in range(n)]
max_s = 50 * (n - 1)

for u, v, a, b in uvab:
    es[u - 1].append(Edge(v - 1, a, b))
    es[v - 1].append(Edge(u - 1, a, b))

dijkstra(n, es, cd, 0, min(max_s, s), max_s)

for i in range(1, n):
    print(min(dp[i]))
