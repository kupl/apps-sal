import heapq
N = int(input())
X = []
Y = []
for i in range(N):
    x, y = map(int, input().split())
    X.append((x, y, i))
    Y.append((y, x, i))
X.sort()
Y.sort()
Edges = list([] for _ in range(N))
for k in range(N - 1):
    xk, yk, ik = X[k]
    xk_, yk_, ik_ = X[k + 1]
    Edges[ik].append((ik_, min(abs(xk - xk_), abs(yk - yk_))))
    Edges[ik_].append((ik, min(abs(xk - xk_), abs(yk - yk_))))
    yk, xk, ik = Y[k]
    yk_, xk_, ik_ = Y[k + 1]
    Edges[ik].append((ik_, min(abs(xk - xk_), abs(yk - yk_))))
    Edges[ik_].append((ik, min(abs(xk - xk_), abs(yk - yk_))))


def prim(Edges, V):
    mst = []
    included = [False] * V
    heap = []
    included[0] = True
    for v, d in Edges[0]:
        heapq.heappush(heap, (d, 0, v))
    while heap:
        d, pre_v, cur_v = heapq.heappop(heap)
        if included[cur_v]:
            continue
        included[cur_v] = True
        mst.append((pre_v, cur_v, d))
        for next_v, dist in Edges[cur_v]:
            if not included[next_v]:
                heapq.heappush(heap, (dist, cur_v, next_v))
    return mst


mst = prim(Edges, N)
ans = 0
for v1, v2, d in mst:
    ans += d

print(ans)
