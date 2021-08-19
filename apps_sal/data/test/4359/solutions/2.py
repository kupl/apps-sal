from itertools import permutations
from math import ceil
times = list((int(input()) for _ in range(5)))
orders = list(permutations(times, 5))
minimum = sum((ceil(time / 10) * 10 for time in times))
for order in orders:
    cnt = order[0]
    for i in range(1, 5):
        cnt += ceil(order[i] / 10) * 10
    minimum = min(minimum, cnt)
print(minimum)
