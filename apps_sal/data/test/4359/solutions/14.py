from math import ceil
orders = list(int(input()) for _ in range(5))
total = 0
maximum = 0

for order in orders:
    time = ceil(order / 10) * 10
    total += time
    delta = time - order
    maximum = max(maximum, delta)
print((total - maximum))
