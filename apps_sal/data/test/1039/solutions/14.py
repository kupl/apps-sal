def main():
    from collections import defaultdict
    from heapq import heappop, heappush
    N = int(input())
    edge = defaultdict(list)
    length = defaultdict(lambda: defaultdict(lambda: 10 ** 20))
    for i in range(N - 1):
        (a, b, c) = map(int, input().split())
        a -= 1
        b -= 1
        edge[a].append(b)
        edge[b].append(a)
        if b < a:
            (a, b) = (b, a)
        length[a][b] = c
    (Q, K) = map(int, input().split())
    K -= 1
    cost = [0] * N
    length[K][K] = 0
    targets = [(0, K)]
    cost = [10 ** 18] * N
    cost[K] = 0
    visited = [False] * N
    while targets:
        (c, t) = heappop(targets)
        if visited[t]:
            continue
        cost[t] = c
        visited[t] = True
        for v in edge[t]:
            if cost[v] > cost[t] + length[min(t, v)][max(t, v)]:
                heappush(targets, (cost[t] + length[min(t, v)][max(t, v)], v))
    out = []
    for i in range(Q):
        (x, y) = map(lambda x: int(x) - 1, input().split())
        out.append(cost[x] + cost[y])
    print('\n'.join(map(str, out)))


main()
