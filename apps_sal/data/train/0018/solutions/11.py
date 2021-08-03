import math
import sys

#sys.stdin = open("in.txt")

t = int(input())
for i in range(t):
    n = int(input())
    n *= 2
    a = (n - 2) * math.pi / n / 2
    r = 1 / 2 * math.tan(a)
    print(2 * r)
