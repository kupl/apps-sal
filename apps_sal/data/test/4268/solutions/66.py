import numpy as np
from itertools import combinations
import math

N, D = list(map(int, input().split()))
X = [list(map(int, input().split())) for i in range(N)]

res = 0
for x, y in combinations(X, 2):
    distance = 0
    for i in range(D):
        distance += (x[i] - y[i])**2
    distance = math.sqrt(distance)
    if(distance.is_integer()):
        res += 1

print(res)
