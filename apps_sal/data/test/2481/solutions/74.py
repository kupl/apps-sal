def main():
    import sys
    from heapq import heappop, heappush

    def input():
        return sys.stdin.readline().rstrip()

    def dijkstra(s):
        inf = 10 ** 6
        dist = [inf] * 10
        dist[1] = 0
        que = [(0, 1)]
        while que:
            (cost, node) = heappop(que)
            if cost > dist[node]:
                continue
            for i in range(10):
                if i == node:
                    continue
                if dist[i] > dist[node] + g[i][node]:
                    dist[i] = dist[node] + g[i][node]
                    heappush(que, (dist[i], i))
        return dist
    (h, w) = map(int, input().split())
    g = [[] for _ in range(10)]
    for i in range(10):
        g[i] = list(map(int, input().split()))
    from collections import defaultdict
    c_lis = defaultdict(int)
    for i in range(h):
        for j in input().split():
            tmp = int(j)
            if abs(tmp) != 1:
                c_lis[tmp] += 1
    dist = dijkstra(1)
    ans = 0
    for key in c_lis:
        ans += c_lis[key] * dist[key]
    print(ans)


def __starting_point():
    main()


__starting_point()
