# refactored Prim's algorithm
# (with dummy 0-node)
import sys


# inf = open('input.txt', 'r')
# reader = (map(int, line.split()) for line in inf)
reader = (list(map(int, s.split())) for s in sys.stdin)

n, = next(reader)
cities = [None]
for _ in range(n):
    x, y = next(reader)
    cities.append((x, y))
cs = [None] + list(next(reader))
ks = [None] + list(next(reader))

n += 1  # extra dummy 0-node (source of power); edge (0, v) = c_v
g = [[None] * n for _ in range(n)]
for i in range(1, n):
    for j in range(i + 1, n):
        wire = ks[i] + ks[j]
        dist = abs(cities[i][0] - cities[j][0]) + \
            abs(cities[i][1] - cities[j][1])
        g[i][j] = g[j][i] = wire * dist
for i in range(1, n):
    g[0][i] = g[i][0] = cs[i]
for i in range(n):
    g[i][i] = float('inf')

totalCost = 0
stations = []
connections = []

connCosts = {i: float('inf') for i in range(n)}
connTo = [-1] * n

start = 0  # starting from dummy node
connCosts[start] = 0
while connCosts:
    # node with min connection cost
    v = min(connCosts, key=connCosts.get)
    if connCosts[v] == float('inf'): break

    fromNode = connTo[v]
    if not fromNode:  # edge (0, v) <=> v-node has station
        totalCost += g[v][fromNode]
        stations.append(v)
    elif fromNode > 0:
        totalCost += g[v][fromNode]
        connections.append((v, fromNode))

    connCosts.pop(v)
    for to, cost in list(connCosts.items()):
        if g[v][to] < connCosts[to]:
            connCosts[to] = g[v][to]
            connTo[to] = v

myprint = sys.stdout.write
myprint(str(totalCost) + '\n')
myprint(str(len(stations)) + '\n')
[myprint(str(st) + ' ') for st in stations];
myprint(str(len(connections)) + '\n')
[myprint(str(c1) + ' ' + str(c2) + '\n') for c1, c2 in connections];

# print(totalCost)
# print(len(stations))
# print(*stations)
# print(len(connections))
# [print(c1, c2) for c1, c2 in connections];

# inf.close()
