import sys
import math
z = list(map(int, input().split()))
s = sum(z)
min_ = s
for i in range(len(z)):
    f = z.count(z[i])
    if f >= 3:
        min_ = min(min_, s - 3 * z[i])
    elif f == 2:
        min_ = min(min_, s - 2 * z[i])
print(min_)
