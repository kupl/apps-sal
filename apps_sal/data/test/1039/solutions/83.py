import sys
import heapq
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline


def in_n():
    return int(readline())


def in_nn():
    return list(map(int, readline().split()))


def in_nl():
    return list(map(int, readline().split()))


def in_na():
    return list(map(int, read().split()))


def in_s():
    return readline().rstrip().decode('utf-8')


INF = 10 ** 18


def dijkstra(N, s0, edge):
    d = [INF] * N
    used = [False] * N
    edgelist = [(0, s0)]
    heapq.heapify(edgelist)
    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        if used[minedge[1]]:
            continue
        v = minedge[1]
        d[v] = minedge[0]
        used[v] = True
        for e in edge[v]:
            if d[e[1]] <= e[0] + d[v] or used[e[1]]:
                continue
            heapq.heappush(edgelist, [e[0] + d[v], e[1]])
    return d


def main():
    N = in_n()
    edge = [[] for _ in range(N)]
    for i in range(N - 1):
        (a, b, c) = in_nn()
        (a, b) = (a - 1, b - 1)
        edge[a].append((c, b))
        edge[b].append((c, a))
    (Q, K) = in_nn()
    d = dijkstra(N, K - 1, edge)
    ans = []
    for i in range(Q):
        (x, y) = in_nn()
        (x, y) = (x - 1, y - 1)
        ans.append(d[x] + d[y])
    print('\n'.join(map(str, ans)))


def __starting_point():
    main()


__starting_point()
