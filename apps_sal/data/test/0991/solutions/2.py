import heapq


def dijkstra_heap(N, S, Smax, edge):
    d = [float('inf')] * (10 ** 4 * N)
    used = [False] * (10 ** 4 * N)
    d[S] = 0
    used[S] = True
    edgelist = []
    for (w, a) in edge[0]:
        (v, sil) = (a // 10 ** 4, a % 10 ** 4)
        if v == 0 and S + sil <= Smax:
            heapq.heappush(edgelist, [w, a + S])
        elif v > 0 and S - sil >= 0:
            heapq.heappush(edgelist, [w, v * 10 ** 4 + (S - sil)])
    while len(edgelist):
        (min_w, min_a) = heapq.heappop(edgelist)
        (min_v, min_sil) = (min_a // 10 ** 4, min_a % 10 ** 4)
        if used[min_a]:
            continue
        d[min_a] = min_w
        used[min_a] = True
        for (w, a) in edge[min_v]:
            (v, sil) = (a // 10 ** 4, a % 10 ** 4)
            if v == min_v and min_sil + sil <= Smax and (not used[a + min_sil]):
                heapq.heappush(edgelist, [min_w + w, a + min_sil])
            elif v != min_v and min_sil - sil >= 0 and (not used[v * 10 ** 4 + (min_sil - sil)]):
                heapq.heappush(edgelist, [min_w + w, v * 10 ** 4 + (min_sil - sil)])
    return d


def solve():
    (N, M, S) = map(int, input().split())
    edge = [[] for _ in range(N)]
    amax = 0
    for i in range(M):
        (u, v, a, b) = map(int, input().split())
        amax = max(amax, a)
        edge[u - 1].append([b, (v - 1) * 10 ** 4 + a])
        edge[v - 1].append([b, (u - 1) * 10 ** 4 + a])
    Smax = (N - 1) * amax
    S = min(S, Smax)
    for i in range(N):
        (c, d) = map(int, input().split())
        edge[i].append([d, i * 10 ** 4 + c])
    D = dijkstra_heap(N, S, Smax, edge)
    ans = [0] * N
    for i in range(1, N):
        ans[i] = min(D[i * 10 ** 4:(i + 1) * 10 ** 4])
    return ans[1:]


print(*solve(), sep='\n')
