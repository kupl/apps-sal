import math
from itertools import permutations


def calc_distance(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    d = math.sqrt(dx * dx + dy * dy)
    return d


N = int(input())

city = [0] * N
for i in range(N):
    city[i] = list(map(int, input().split()))

mtx = [0 for i in range(N)] * N

mtx = [[calc_distance(a, b) for a in city] for b in city]


all_distance = 0
paths = permutations([i for i in range(N)])
cnt = 0
for pt in paths:
    distance = 0
    for idx in range(1, len(pt)):
        distance += mtx[pt[idx]][pt[idx - 1]]

    all_distance += distance
    cnt += 1

all_distance /= cnt


print(all_distance)
