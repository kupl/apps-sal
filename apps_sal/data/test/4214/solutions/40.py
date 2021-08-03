import math
import itertools


def calc(x1y1, x2y2):
    x1, y1 = x1y1
    x2, y2 = x2y2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


N = int(input())
addresses = []

for _ in range(N):
    addresses.append(list(map(int, input().split())))

ways = list(itertools.permutations(list(range(N))))

ans = 0
for x in ways:
    dist = 0
    for i in range(N - 1):
        dist += calc(addresses[x[i]], addresses[x[i + 1]])
    ans += dist

print((ans / len(ways)))
