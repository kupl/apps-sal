import sys
from collections import defaultdict
from heapq import heapify, heappush, heappop
readline = sys.stdin.readline


def main():
    (N, M, R) = list(map(int, readline().split()))
    r = list(map(int, readline().split()))
    ew = [tuple(map(int, readline().split())) for _ in range(M)]
    edges = defaultdict(list)
    wt = defaultdict(int)
    for e in ew:
        edges[e[0]].append(e[1])
        edges[e[1]].append(e[0])
        wt[e[0], e[1]] = e[2]
        wt[e[1], e[0]] = e[2]
    inf = float('inf')

    def dijkstra(v):
        dist = [inf] * (N + 1)
        dist[v] = 0
        vw = [(0, v)]
        heapify(vw)
        while vw:
            cvw = heappop(vw)
            if cvw[0] > dist[cvw[1]]:
                continue
            for w in edges[cvw[1]]:
                cand = cvw[0] + wt[cvw[1], w]
                if dist[w] > cand:
                    dist[w] = cand
                    heappush(vw, (cand, w))
        return dist
    distdict = dict(((v, dijkstra(v)) for v in r))
    mindist = inf

    def permlist(lst):
        tmp = []
        if not lst:
            return [[]]
        for (i, x) in enumerate(lst):
            lstx = lst[:i] + lst[i + 1:]
            ret = permlist(lstx)
            for e in ret:
                e.append(x)
            tmp.extend(ret)
        return tmp
    pathlist = [sum([distdict[v][w] for (v, w) in zip(lst, lst[1:])]) for lst in permlist(r)]
    print(min(pathlist))


def __starting_point():
    main()


__starting_point()
