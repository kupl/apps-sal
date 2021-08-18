import math
import sys


t = int(input())
for i in range(t):
    n = int(input())
    n *= 2
    a = (n - 2) * math.pi / n / 2
    r = 1 / 2 * math.tan(a)
    print(2 * r)
