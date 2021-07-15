import itertools


def dijkstra(v, G):
    import heapq

    ret = [10 ** 10] * len(G)
    ret[v] = 0
    q = [(ret[i], i) for i in range(len(G))]
    heapq.heapify(q)

    while len(q):
        tmpr, u = heapq.heappop(q)
        if tmpr == ret[u]:
            for w, l in G[u]:
                if ret[w] > ret[u] + l:
                    ret[w] = ret[u] + l
                    heapq.heappush(q, (ret[w], w))
    return ret


N, M, R = list(map(int, input().split()))
r = list(map(int, input().split()))
NE = [[] for _ in range(N)]
for _ in range(M):
    A, B, C = list(map(int, input().split()))
    NE[A - 1].append((B - 1, C))
    NE[B - 1].append((A - 1, C))

RE = [[0] * R for _ in range(R)]
for iR in range(R):
    for jR in range(iR + 1, R):
        lR = dijkstra(r[iR] - 1, NE)[r[jR] - 1]
        RE[iR][jR] = lR
        RE[jR][iR] = lR

ans = 10 ** 10
for p in itertools.permutations(list(range(R))):
    ans = min(ans, sum([RE[p[i]][p[i + 1]] for i in range(R - 1)]))

print(ans)

