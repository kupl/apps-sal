from heapq import heapify, heappop, heappush
from sys import stdin
pin = stdin.readline
INF = 1000000000000000000
V = 0
G = [[] for _ in [0] * 100000]
d = [INF] * 100000


def dijkstra(s):
    que = []
    heapify(que)
    d[s] = 0
    heappush(que, [0, s])
    while que:
        p = heappop(que)
        v = p[1]
        if d[v] < p[0]:
            continue
        for i in range(len(G[v])):
            e = G[v][i]
            if d[e[0]] > d[v] + e[1]:
                d[e[0]] = d[v] + e[1]
                heappush(que, [d[e[0]], e[0]])
    return


def main():
    a, b, x, y = map(int, pin().split())
    V = 200
    a -= 1
    b -= 1
    for i in range(100):
        G[i].append([i + 100, x])
        G[i + 100].append([i, x])
    for i in range(99):
        G[i + 1].append([i + 100, x])
        G[i + 100].append([i + 1, x])
    for i in range(99):
        G[i + 1].append([i, y])
        G[i].append([i + 1, y])
        G[i + 101].append([i + 100, y])
        G[i + 100].append([i + 101, y])
    dijkstra(a)
    print(d[b + 100])
    return


main()
