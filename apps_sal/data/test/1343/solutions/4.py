line1 = input().split()
n = int(line1[0])  # Num cities
m = int(line1[1])  # Num roads
k = int(line1[2])  # Num storagecities

roads = []
for i in range(m):
    line = input().split()
    line[0], line[1], line[2] = int(line[0]), int(line[1]), int(line[2])
    roads.append(line)


cities = {}
for i in range(n):
    cities[i + 1] = False

if (k > 0):
    line = input().split()
    for c in line:
        cities[int(c)] = True

best = -1

for road in roads:
    u = road[0]
    v = road[1]
    l = road[2]
    if cities[u] == (not cities[v]):
        if best == -1:
            best = l
        else:
            best = min(best, l)
print(best)
