from math import gcd
from functools import reduce
n, x = map(int, input().split())
xlist = list(map(int, input().split()))
if n == 1:
    print(abs(xlist[0] - x))
    return
ylist = []
for i in range(n):
    ylist.append(abs(xlist[i] - x))
print(reduce(gcd, ylist))
