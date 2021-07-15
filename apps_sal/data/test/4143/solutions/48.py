# author:  Taichicchi
# created: 28.09.2020 00:14:38

import sys
from math import ceil
n = int(input())
m = 10 ** 18
for i in range(5):
    m = min(m, int(input()))

print((ceil(n / m) + 4))

