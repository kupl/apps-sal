import math
from itertools import accumulate

n = int(input())
a = list(map(int, input().split()))

fromleft = list(accumulate(a, math.gcd))
a.reverse()
fromright = list(accumulate(a, math.gcd))
fromright.reverse()
a.reverse()

gcd = []

gcd.append(fromright[1])
for i in range(1, n - 1):
    gcd.append(math.gcd(fromleft[i - 1], fromright[i + 1]))

gcd.append(fromleft[n - 2])

if n == 2:
    print((max(a[1], a[0])))
else:
    print((max(gcd)))
