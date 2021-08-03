import collections
import heapq


def __starting_point():
    n, m = [int(x) for x in input().split()]
    G = collections.defaultdict(list)
    road = []
    for i in range(m):
        s, e, f = [int(x) for x in input().split()]
        road.append((s, e, f))
        G[s].append((e, f))
        G[e].append((s, f))

    def dijkstra(s, e):
        d = [(float('inf'), float('inf')) for _ in range(n + 1)]
        pre = [-1 for _ in range(n + 1)]
        d[s] = (0, 0)
        hq = [(0, 0, s)]
        while hq:
            dis, cost, p = heapq.heappop(hq)
            if d[p] < (dis, cost):
                continue
            for e, f in G[p]:
                cost_e = cost + (1 if not f else 0)
                dis_e = dis + 1
                if (dis_e, cost_e) < d[e]:
                    d[e] = (dis_e, cost_e)
                    pre[e] = p
                    heapq.heappush(hq, (dis_e, cost_e, e))
        return pre
    pre = dijkstra(1, n)
    q = n
    path = []
    while q != -1:
        path.append(q)
        q = pre[q]
    pairs = set()
    for i in range(len(path) - 1):
        pairs.add((path[i], path[i + 1]))
    k = 0
    ans = []
    for s, e, f in road:
        if ((s, e) in pairs or (e, s) in pairs) and f == 0:
            k += 1
            ans.append((s, e, 1))
        elif ((s, e) not in pairs and (e, s) not in pairs) and f == 1:
            k += 1
            ans.append((s, e, 0))
    print(k)
    for s, e, f in ans:
        print(s, e, f)


__starting_point()
