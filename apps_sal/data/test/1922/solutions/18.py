# author:  Taichicchi
# created: 28.09.2020 23:24:54

import sys

n, m = list(map(int, input().split()))

if (n == 1) & (m == 1):
    print((1))
elif n == 1:
    print((m - 2))
elif m == 1:
    print((n - 2))
else:
    print(((n - 2) * (m - 2)))
