import heapq
def prim():
    used = [True]*n
    edgelist = []
    for e in edge[0]:
        heapq.heappush(edgelist, e)
        used[0] = False
    res = 0
    while len(edgelist) != 0:
        minedge = heapq.heappop(edgelist)
        if not  used[minedge[1]]:
            continue
        v = minedge[1]
        used[v] = False
        for e in edge[v]:
            if used[e[1]]:
                heapq.heappush(edgelist, e)
        res += minedge[0]
    return res
n = int(input())
P = []
for i in range(n):
    x, y = map(int, input().split())
    P.append((x, y, i))
P.sort()
edge = [[] for _ in range(n)]
for i in range(n-1):
    d = min(abs(P[i+1][0]-P[i][0]), abs(P[i+1][1]-P[i][1]))
    edge[P[i][2]].append((d, P[i+1][2]))
    edge[P[i+1][2]].append((d, P[i][2]))
P.sort(key = lambda x: x[1])
for i in range(n-1):
    d = min(abs(P[i+1][0]-P[i][0]), abs(P[i+1][1]-P[i][1]))
    edge[P[i][2]].append((d, P[i+1][2]))
    edge[P[i+1][2]].append((d, P[i][2]))
print(prim())
