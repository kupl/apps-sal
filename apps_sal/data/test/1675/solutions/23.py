import sys
import math

n = int(sys.stdin.readline())

a = [0] * 100000
b = [0] * 100000

d = []
for i in range(n):
    h, g = [int(x) for x in (sys.stdin.readline()).split()]
    d.append((h - 1, g - 1))
    a[h - 1] += 1
    b[g - 1] += 1
   
for i in d:
    print(str((n - 1) + (a[i[1]])) + " " + str(n - a[i[1]] - 1))
