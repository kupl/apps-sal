import sys
import heapq

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: list(map(int, readline().split()))
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: list(map(int, read().split()))
in_s = lambda: readline().rstrip().decode('utf-8')


INF = 10**18


def dijkstra(N, s0, edge):

    d = [INF] * N  # 始点からの距離
    used = [False] * N  # 探索済みリスト
    edgelist = [(0, s0)]  # 始点はコスト0で初期化
    heapq.heapify(edgelist)  # ヒープにpush

    while len(edgelist):
        minedge = heapq.heappop(edgelist)
        if used[minedge[1]]:
            continue
        v = minedge[1]
        d[v] = minedge[0]
        used[v] = True
        for e in edge[v]:
            if d[e[1]] <= (e[0] + d[v]) or used[e[1]]:
                continue
            heapq.heappush(edgelist, [e[0] + d[v], e[1]])
    return d


def main():
    N = in_n()

    edge = [[]for _ in range(N)]
    for i in range(N - 1):
        a, b, c = in_nn()
        a, b = a - 1, b - 1
        edge[a].append((c, b))
        edge[b].append((c, a))

    Q, K = in_nn()
    d = dijkstra(N, K - 1, edge)

    ans = []
    for i in range(Q):
        x, y = in_nn()
        x, y = x - 1, y - 1
        ans.append(d[x] + d[y])

    print(('\n'.join(map(str, ans))))


def __starting_point():
    main()


__starting_point()
