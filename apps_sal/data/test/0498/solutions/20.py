from math import *
(n, m, k) = [int(x) for x in input().split()]
tmp1 = ceil(k / (2 * m))
tmp2 = k - (tmp1 - 1) * 2 * m
tmp3 = ceil(tmp2 / 2)
if k % 2 == 0:
    print(tmp1, tmp3, 'R')
else:
    print(tmp1, tmp3, 'L')
