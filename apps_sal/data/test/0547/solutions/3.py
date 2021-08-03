# def hh(a):
#    return -a

import sys
import math
n, k = list(map(int, input().split()))
z = [0] * n
for i in range(n):
    z[i] = len(input())
#z.sort(key = hh)
passw = len(input())
bef = 0
same = 0
for i in range(n):
    if z[i] == passw:
        same += 1
    elif z[i] < passw:
        bef += 1
print((bef + 1) + 5 * (bef // k), (bef + same) + 5 * ((bef + same - 1) // k))
