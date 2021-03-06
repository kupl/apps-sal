import sys
sys.setrecursionlimit(10 ** 9)
(N, M) = map(int, input().split())


def find_negative_loop(n, w, es):
    dist = [float('inf')] * n
    dist[1] = 0
    for i in range(n):
        for j in range(w):
            e = es[j]
            if dist[e[1]] > dist[e[0]] + e[2]:
                dist[e[1]] = dist[e[0]] + e[2]
                if i == n - 1:
                    return True
    return False


def shortest_path(s, n, w, es):
    dist = [float('inf')] * n
    dist[s] = 0
    while True:
        update = False
        for (p, q, r) in es:
            if dist[p] != float('inf') and dist[q] > dist[p] + r:
                dist[q] = dist[p] + r
                update = True
        if not update:
            break
    return dist


graph = [[] for _ in range(N + 1)]
elist = []
for _ in range(M):
    (a, b, c) = map(int, input().split())
    graph[a].append(b)
    elist.append((a, b, -c))
visited = [None] * (N + 1)


def check_reachable(u):
    if u == N:
        reachable[u] = True
        return True
    visited[u] = True
    cnt = 0
    for v in graph[u]:
        if not visited[v]:
            ret = check_reachable(v)
            if ret:
                reachable[u] = True
                cnt += 1
    if cnt > 0:
        return True
    else:
        return False


reachable = [None] * (N + 1)
for i in range(1, N + 1):
    if reachable[i] == None:
        visited = [False] * (N + 1)
        check_reachable(i)
elist2 = []
for (a, b, nc) in elist:
    if reachable[b]:
        elist2.append((a, b, nc))
M2 = len(elist2)
res1 = find_negative_loop(N + 1, M2, elist2)
if res1:
    print('inf')
else:
    res2 = shortest_path(1, N + 1, M2, elist2)
    print(-res2[N])
