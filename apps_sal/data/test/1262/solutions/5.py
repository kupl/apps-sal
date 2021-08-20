import sys
reader = (list(map(int, s.split())) for s in sys.stdin)
(n,) = next(reader)
locs = [tuple(next(reader)) for _ in range(n)]
cs = list(next(reader))
ks = list(next(reader))
totalCost = 0
stations = []
connections = []
connCosts = {i: cost for (i, cost) in enumerate(cs)}
connTo = [-1] * n
while connCosts:
    v = min(connCosts, key=connCosts.get)
    totalCost += connCosts[v]
    if connCosts[v] < cs[v]:
        to = connTo[v]
        connections.append((v, to))
    else:
        stations.append(v)
    connCosts.pop(v)
    for (to, cost) in list(connCosts.items()):
        wire = ks[v] + ks[to]
        dist = abs(locs[v][0] - locs[to][0]) + abs(locs[v][1] - locs[to][1])
        newCost = wire * dist
        if connCosts[to] > newCost:
            connCosts[to] = newCost
            connTo[to] = v
myprint = sys.stdout.write
myprint(str(totalCost) + '\n')
myprint(str(len(stations)) + '\n')
[myprint(str(st + 1) + ' ') for st in stations]
myprint(str(len(connections)) + '\n')
[myprint(str(c1 + 1) + ' ' + str(c2 + 1) + '\n') for (c1, c2) in connections]
