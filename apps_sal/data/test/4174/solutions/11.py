from itertools import accumulate
from bisect import *
(N, X) = list(map(int, input().split()))
L = list(tuple(map(int, input().split())))
acc = sorted(list(accumulate(L)) + [0])
n = bisect_right(acc, X)
print(n)
