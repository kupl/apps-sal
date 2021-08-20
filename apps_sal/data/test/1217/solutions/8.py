from math import ceil, modf
from bisect import bisect
(n, m) = [int(s) for s in input().split()]
a = [int(s) for s in input().split()]
a.sort()
for i in input().split():
    print(bisect(a, int(i)), end=' ')
