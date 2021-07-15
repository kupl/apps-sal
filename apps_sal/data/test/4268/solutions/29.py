import numpy as np
from itertools import combinations
import math

N, D = list(map(int, input().split()))
X = [list(map(int, input().split())) for i in range(N)]

res = 0
for x, y in combinations(X, 2):
    if((sum((np.array(x)-np.array(y))**2)**0.5).is_integer()):
        res += 1
print(res)

