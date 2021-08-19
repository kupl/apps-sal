import itertools
import math
n = int(input())
path = []
for i in range(n):
    (x, y) = map(int, input().split())
    path.append([x, y])
distance = []
visitedPath = list(itertools.permutations(path))
for vp in visitedPath:
    routeDistance = 0
    for i in range(len(vp) - 1):
        routeDistance += math.sqrt((vp[i][0] - vp[i + 1][0]) ** 2 + (vp[i][1] - vp[i + 1][1]) ** 2)
    distance.append(routeDistance)
print(sum(distance) / len(distance))
