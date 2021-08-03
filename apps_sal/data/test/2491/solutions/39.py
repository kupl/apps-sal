def BellmanFord():
    def BF(s, n, edge, inf=float("inf")):
        d = [inf for i in range(n)]
        d[s] = 0
        for i in range(n):
            for before, after, dist in edge:
                if before != inf:
                    d[after] = min(d[after], d[before] + dist)
            if i == n - 2:
                t = d[:]
            elif i == n - 1:
                for i, j in enumerate(d):
                    if j != t[i]:
                        d[i] = -inf
        return list(map(lambda x: -x, d))
    n, m = map(int, input().split())
    inf = 10 ** 20
    edge = [list(map(int, input().split())) for i in range(m)]
    edge = [[x - 1, y - 1, -z] for x, y, z in edge]
    l = BF(0, n, edge)
    print(l[-1] if l[-1] < inf else "inf")


BellmanFord()
