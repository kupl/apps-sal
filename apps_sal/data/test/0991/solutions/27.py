from heapq import heappop, heappush
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

# グラフを拡張してダイクストラ法を使う


def main():
    N, M, S = list(map(int, readline().split()))

    E = [[] for _ in range(N + 1)]
    for _ in range(M):
        u, v, a, b = list(map(int, readline().split()))
        E[u].append((v, a, b))
        E[v].append((u, a, b))

    cd = list(map(int, read().split()))
    CD = []
    for c, d in zip(*[iter(cd)] * 2):
        CD.append((c, d))

    # Dijkstra
    # d[v][s] := 頂点vで,所持金sとなる最小の所要時間
    if S > 2500:
        S = 2500 - 1
    INF = 10**15
    d = [[INF] * 2500 for _ in range(N + 1)]
    d[1][S] = 0

    Q = []
    heappush(Q, (0, S, 1))  # (所要時間, 所持金, 頂点)

    while Q:
        time, s, u = heappop(Q)
        if time > d[u][s]:
            continue

        c_u, d_u = CD[u - 1]
        if s + c_u < 2500 and time + d_u < d[u][s + c_u]:
            d[u][s + c_u] = time + d_u
            heappush(Q, (time + d_u, s + c_u, u))

        for v, a, b in E[u]:
            if s >= a and time + b < d[v][s - a]:
                d[v][s - a] = time + b
                heappush(Q, (time + b, s - a, v))

    for i in range(2, N + 1):
        print((min(d[i])))


def __starting_point():
    main()


__starting_point()
