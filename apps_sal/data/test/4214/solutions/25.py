import numpy as np
import itertools
import math


def calc_dist(pos1, pos2):
    (x1, y1) = pos1
    (x2, y2) = pos2
    return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))


N = int(input())
distance_mat = [[-1000 for _ in range(N)] for _ in range(N)]
pos = []
for _ in range(N):
    pos.append(list(map(int, input().split())))
perms = itertools.permutations(list(range(N)), N)
result = []
for perm in perms:
    dist_sum = 0
    for i in range(1, N):
        source = perm[i - 1]
        sink = perm[i]
        if distance_mat[source][sink] == -1000:
            dist = calc_dist(pos[source], pos[sink])
            distance_mat[source][sink] = dist
            distance_mat[sink][source] = dist
        else:
            dist = distance_mat[source][sink]
        dist_sum += dist
    result.append(dist_sum)
print(np.average(result))
