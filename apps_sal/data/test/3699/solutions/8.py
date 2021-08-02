import math
import sys

ax, ay, bx, by, tx, ty = list(map(float, input().split()))
n = int(input())


def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


cost = 0
bottleCoord = []
for i in range(0, n):
    x, y = list(map(float, input().split()))
    cost += 2 * dist(tx, ty, x, y)
    bottleCoord.append((x, y))

asCost = [(0, -1)]
bsCost = [(0, -1)]

for i in range(0, n):
    asCost.append((dist(ax, ay, bottleCoord[i][0], bottleCoord[i][1]) - dist(bottleCoord[i][0], bottleCoord[i][1], tx, ty), i))
    bsCost.append((dist(bx, by, bottleCoord[i][0], bottleCoord[i][1]) - dist(bottleCoord[i][0], bottleCoord[i][1], tx, ty), i))

asCost.sort()
bsCost.sort()
costTmpIndiv = sys.maxsize

for i in range(0, min(len(asCost), 5)):
    for j in range(0, min(len(bsCost), 5)):
        if (asCost[i][1] != bsCost[j][1]):
            costTmpIndiv = min(costTmpIndiv, asCost[i][0] + bsCost[j][0])

print(cost + costTmpIndiv)
