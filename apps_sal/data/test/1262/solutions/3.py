import sys

# inf = open('input.txt', 'r')
# reader = (map(int, line.split()) for line in inf)
reader = (map(int, s.split()) for s in sys.stdin)

n, = next(reader)
cities = [None]
for _ in range(n):
    x, y = next(reader)
    cities.append((x, y))
cs = [None] + list(next(reader))
ks = [None] + list(next(reader))

n += 1
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

used = [False] * n
min_e = [float('inf')] * n
sel_e = [-1] * n

start = 0  # starting from 0-node (dummy node)
min_e[start] = 0
for i in range(n):
    v = -1
    for j in range(n):
        if (not used[j] and (v == -1 or min_e[j] < min_e[v])):
            v = j
#     if min_e[v] == float('inf'): break
    used[v] = True

    fromNode = sel_e[v]
    if not fromNode:  # edge (0, v) <=> v-node has station
        totalCost += g[v][fromNode]
        stations.append(v)
    elif fromNode > 0:
        totalCost += g[v][fromNode]
        connections.append((v, fromNode))

    for to in range(n):
        if g[v][to] < min_e[to]:
            min_e[to] = g[v][to]
            sel_e[to] = v

print(totalCost)
print(len(stations))
print(*stations)
print(len(connections))
[print(c1, c2) for c1, c2 in connections];

# inf.close()
