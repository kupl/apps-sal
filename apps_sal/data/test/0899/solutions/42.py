n, m = map(int, input().split())
graph = [[float('inf')]*n for i in range(n)]
u_s=[]
v_s=[]
w_s=[]
for _ in range(m):
    u, v, w = map(int, input().split())
    u_s.append(u-1)
    v_s.append(v-1)
    w_s.append(w)
    graph[u-1][v-1] = w
    graph[v-1][u-1] = w
for i in range(n):
    graph[i][i] = 0


def warshall_floyd(d):
    # d[i][j] : i から j への最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])
    return d

dist=warshall_floyd(graph)

ans=0
for i in range(m):
    if w_s[i]>dist[u_s[i]][v_s[i]]:
        ans+=1

print(ans)
