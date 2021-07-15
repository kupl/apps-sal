#ダイクストラ法
import heapq
def dijkstra(s):
    p=[x for x in range(n)]#親の記憶
    hq = [(0, s)]
    heapq.heapify(hq) # リストを優先度付きキューに変換
    cost = [float('inf')] * n # 行ったことのないところはinf
    cost[s] = 0 # 開始地点は0
    while hq:
        c, v = heapq.heappop(hq)
        if c > cost[v]: # コストが現在のコストよりも高ければスルー
            continue
        for d, u in e[v]:
            tmp = d + cost[v]
            if tmp < cost[u]:
                cost[u] = tmp
                p[u]=v
                heapq.heappush(hq, (tmp, u))
    return p

n,m = list(map(int,input().split()))
#重み付き有向グラフの隣接リストe(重み=1)
e = [[] for _ in range(n)]
t=1
for _ in range(m):
    a,b= list(map(int,input().split()))
    a,b = a-1, b-1
    e[a].append((t, b))
    e[b].append((t, a))

ans = dijkstra(0)
print('Yes')
for i in range(1,n):
  print((ans[i]+1))

