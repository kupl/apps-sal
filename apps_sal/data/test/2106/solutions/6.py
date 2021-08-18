import sys
import math
m, k = [int(i) for i in sys.stdin.readline().split()]
d = [int(i) for i in sys.stdin.readline().split()]
s = [int(i) for i in sys.stdin.readline().split()]


time = 0
oil = 0
max_val = 0
for i, val in enumerate(d):
    oil += s[i]
    if s[i] > max_val:
        max_val = s[i]
    if val <= oil:
        time += val
        oil -= val
    else:
        left = val - oil
        times = math.ceil(left / max_val)
        oil += times * max_val
        time += val + times * k
        oil -= val
print(time)
