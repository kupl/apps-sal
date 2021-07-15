import sys
input = lambda: sys.stdin.readline().strip()
from math import *

t = int(input())
for i in range(t):
    a, b, c, d, e = list(map(int, input().split()))
    if ceil(a/c)+ceil(b/d)<=e:
        print(ceil(a/c), ceil(b/d))
    else:
        print(-1)

