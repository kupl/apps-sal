import sys
from math import *
from fractions import gcd
def readints(): return list(map(int, input().strip('\n').split()))


n = int(input())
a = list(readints())
a.sort()
if sum(a[:n]) == sum(a[n:]):
    print(-1)
else:
    buf = ''
    for x in a:
        buf += str(x) + ' '
    print(buf)
