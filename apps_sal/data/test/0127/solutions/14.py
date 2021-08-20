import math
import re
(n, f) = list(map(int, input().split()))
k = []
l = []
d = []
d1 = []
for i in range(n):
    (k, l) = list(map(int, input().split()))
    if k >= l:
        d.append(0)
        d1.append(l)
    elif 2 * k >= l:
        d.append(l - k)
        d1.append(k)
    else:
        d.append(k)
        d1.append(k)
d = sorted(d, reverse=True)
print(sum(d[:f]) + sum(d1))
