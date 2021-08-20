from itertools import permutations
import math
T = [int(input()) for i in range(5)]
res = float('INF')
for order in permutations(T):
    total = order[0]
    for i in range(1, 5):
        total += math.ceil(order[i] / 10) * 10
    res = min(res, total)
print(res)
