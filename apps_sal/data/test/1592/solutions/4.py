import sys
import math
n = int(input())
(a, b) = list(map(int, input().split()))
vmax = b
for i in range(1, n):
    (c, d) = list(map(int, input().split()))
    b = max(0, b - (c - a))
    a = c
    b += d
    vmax = max(b, vmax)
print(a + b, vmax)
