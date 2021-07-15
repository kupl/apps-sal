import heapq


INF = float('inf')
N, M = map(int, input().split())
to = [[] for _ in range(N)]

#sides[i][j] : i-->jへ向かう辺を通るかどうかを保持
# 1 : 通る、0 : 通らない
sides = [[0] * N for _ in range(N)]


for _ in range(M):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    to[a].append((c, b))
    to[b].append((c, a))
    sides[a][b] = 1 #a, b間に辺がある
    sides[b][a] = 1


# dijkstraで最短経路木をつくる
def dijkstra(s):
    hq = [(0, s)]
    heapq.heapify(hq) 
    cost = [[INF, []] for i in range(N)]
    cost[s][0] = 0
    while hq:
        c, v = heapq.heappop(hq)
        if c > cost[v][0]:
            continue
        for d, u in to[v]:
            tmp = d + cost[v][0]
            if tmp < cost[u][0]:
                cost[u][0] = tmp
                cost[u][1] = [v] # 更新する場合は直前の頂点を保持
                heapq.heappush(hq, (tmp, u))
            elif tmp == cost[u][0]:
                cost[u][1].append(v) # 距離が等しい場合はリストで直前の頂点を保持  
                heapq.heappush(hq, (tmp, u))
    return cost


# 作成した最短経路木を探索して、通る辺を調べる
def dfs(v, tree, p=-1):
    if p >= 0:
        sides[v][p] = 0
        sides[p][v] = 0
    for nv in tree[v][1]:
        dfs(nv, tree, v)


def main():
    for s in range(N):
        tree = dijkstra(s)
        for g in range(N):
            dfs(g, tree)

    print(sum(sum(column) for column in sides) // 2)


def __starting_point():
    main()
__starting_point()
