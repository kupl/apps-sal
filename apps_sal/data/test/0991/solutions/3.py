import heapq


def dijkstra_heap():
    used = [-1] * (2451 * n)
    edgelist = []
    heapq.heappush(edgelist, [0, ss])
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        if used[minedge[1]] != -1:
            continue
        v = minedge[1]
        kai = minedge[0]
        mai = v % 2451
        used[v] = kai
        for e in edge[v // 2451]:
            if mai - e[1] >= 0:
                sss = mai - e[1]
                if used[e[2] * 2451 + sss] == -1:
                    heapq.heappush(edgelist, [e[0] + kai, e[2] * 2451 + sss])
        if mai + cd[v // 2451][0] <= 2450:
            if used[v + cd[v // 2451][0]] == -1:
                heapq.heappush(edgelist, [kai + cd[v // 2451][1], v + cd[v // 2451][0]])
    return used


################################
n, m, ss = map(int, input().split())
ss = min(2450, ss)
edge = [[] for i in range(n)]

for i in range(m):
    x, y, a, b = map(int, input().split())
    edge[x - 1].append([b, a, y - 1])
    edge[y - 1].append([b, a, x - 1])
cd = []
for i in range(n):
    cd.append(list(map(int, input().split())))
pp = dijkstra_heap()
for i in range(1, n):
    ans = 10**20
    for j in range(2451):
        if pp[i * 2451 + j] != -1:
            ans = min(ans, pp[i * 2451 + j])
    print(ans)
