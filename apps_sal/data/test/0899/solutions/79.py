import sys
import heapq
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = list(map(int, input().split()))
    edge = [[] for _ in range(n)]
    k = []
    for _ in range(m):
        a, b, c = list(map(int, input().split()))
        edge[a - 1].append([c, b - 1])
        edge[b - 1].append([c, a - 1])
        k.append([c, a - 1, b - 1])

    def dijkstra_heap(s):
        d = [f_inf] * n
        used = [True] * n
        d[s] = 0
        used[s] = False
        edgelist = []
        for e in edge[s]:
            heapq.heappush(edgelist, e)
        while len(edgelist):
            minedge = heapq.heappop(edgelist)
            if not used[minedge[1]]:
                continue
            v = minedge[1]
            d[v] = minedge[0]
            used[v] = False
            for e in edge[v]:
                if used[e[1]]:
                    heapq.heappush(edgelist, [e[0] + d[v], e[1]])
        return d

    used = set()
    for i in range(n):
        dist = dijkstra_heap(i)
        for d, to, fr in k:
            if dist[to] + d == dist[fr]:
                used.add((to, fr))

    print((len(k) - len(used)))

def __starting_point():
    resolve()

__starting_point()
