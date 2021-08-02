import sys
import math

n = int(sys.stdin.readline())
a = [int(x) for x in (sys.stdin.readline()).split()]

a.sort()
res = 0
for i in range(n):
    res += int(math.fabs(i + 1 - a[i]))

print(res)
