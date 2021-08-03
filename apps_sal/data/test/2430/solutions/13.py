import sys
import math

n = int(sys.stdin.readline())

c = 0
res = 0
for i in range(n):
    v = int(sys.stdin.readline())
    res += int(math.fabs(c - v))
    c = v

print(res + n + (n - 1))
