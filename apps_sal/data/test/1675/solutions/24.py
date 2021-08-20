import sys
import math
n = int(sys.stdin.readline())
a = [0] * 100000
d = []
for i in range(n):
    (h, g) = [int(x) for x in sys.stdin.readline().split()]
    d.append(g - 1)
    a[h - 1] += 1
for i in d:
    print(str(n - 1 + a[i]) + ' ' + str(n - a[i] - 1))
