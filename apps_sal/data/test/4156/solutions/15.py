import sys

_, max_capacity = list(map(int, next(sys.stdin).rstrip().split()))

xs = list(map(int, next(sys.stdin).rstrip().split()))

current = 0
max_x = 0
min_x = 0

for x in xs:
    current += x
    max_x = max(max_x, current)
    min_x = min(min_x, current)

calibration = max_x - min_x

if calibration > max_capacity:
    print(0)
else:
    print(max_capacity - calibration + 1)
