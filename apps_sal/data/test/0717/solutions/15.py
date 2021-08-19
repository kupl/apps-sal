import math
n = int(input())
schedules = []
for _ in range(n):
    schedules.append(tuple(map(int, input().split())))
day = 0
for (start, period) in schedules:
    lower_bound = (day - start) / period
    if lower_bound.is_integer():
        lower_bound = int(lower_bound + 1)
    else:
        lower_bound = math.ceil(lower_bound)
    lower_bound = max(0, lower_bound)
    day = start + period * lower_bound
print(day)
