from itertools import permutations
import math
INF = float('inf')
menu = 5
times = [int(input()) for i in range(menu)]
orders = list(permutations(times, menu))
minimum = INF
for order in orders:
    total = order[0]
    for i in range(1, menu):
        total += math.ceil(order[i]/10)*10
    minimum = min(minimum, total)
print(minimum)
