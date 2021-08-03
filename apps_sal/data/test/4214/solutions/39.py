from itertools import permutations
from math import sqrt
N = int(input())
xy = [input().split() for _ in range(N)]
xy = [[int(x), int(y)] for x, y in xy]
distance = 0
P = list(permutations(xy, N))
for r in P:
    temp = None
    for i in r:
        if not temp:
            temp = i
            continue
        distance += sqrt((temp[0] - i[0])**2 + (temp[1] - i[1])**2)
        temp = i
print(distance / len(P))
