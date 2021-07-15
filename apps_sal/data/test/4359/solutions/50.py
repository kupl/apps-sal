from itertools import permutations
from math import ceil

times = [int(input()) for _ in range(5)]
orders = list(permutations(times))
minimum = sum(ceil(time/10)*10 for time in times)

for order in orders:
    total = order[0]
    for i in range(1, 5):
        total += ceil(order[i]/10)*10
    minimum = min(minimum, total)
print(minimum)


