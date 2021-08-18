import math
import collections
n = int(input())
K = 0
l = 0
r = n + 1
m = 0
while(r - l > 1):
    m = ((l + r) // 2)
    if ((m * (m + 1)) // 2) > n + 1:
        r = m
    else:
        l = m
print((n - l + 1))
