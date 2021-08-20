import functools
import itertools
import math
n = int(input())
poss = []
for _ in range(n):
    (x, y) = map(int, input().split())
    poss.append((x, y))


def dist(i, j):
    (xi, yi) = poss[i]
    (xj, yj) = poss[j]
    return math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2)


totaldist = 0.0
for order in itertools.permutations(range(n)):
    for i in range(1, n):
        totaldist += dist(order[i - 1], order[i])
totaldist /= functools.reduce(lambda x, y: x * y, range(1, n + 1))
print(totaldist)
