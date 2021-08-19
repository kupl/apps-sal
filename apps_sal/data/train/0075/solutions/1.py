import math
import sys
t = int(input())
for i in range(t):
    n = int(input())
    n *= 2
    a = (n - 2) * math.pi / n / 2
    r = 1 / 2 / math.cos(a)
    a2 = (math.pi / 2 - a) / 2
    r2 = r * math.cos(a2)
    print(r2 * 2)
