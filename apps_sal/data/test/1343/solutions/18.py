def update_min(v):
    nonlocal min_
    for u, w in list(graph[v].items()):
        if not is_whouse[u]:
            min_ = min(min_, w)

min_ = 10000000000000000
n, m, k = list(map(int, input().split()))
graph = [dict() for i in range(n)]
for i in range(m):
    u, v, l = list(map(int, input().split()))
    u -= 1
    v -= 1
    if v in list(graph[u].keys()):
        graph[u][v] = min(l, graph[u][v])
    else:
        graph[u][v] = l
    if u in list(graph[v].keys()):
        graph[v][u] = min(l, graph[v][u])
    else:
        graph[v][u] = l
if k:
    whouses = list(map(int, input().split()))

    is_whouse = [False for i in range(n)]
    for w in whouses:
        is_whouse[w - 1] = True
    for w in whouses:
        update_min(w - 1)
    if min_ == 10000000000000000:
        print(-1)
    else:
        print(min_)
else:
    print(-1)

