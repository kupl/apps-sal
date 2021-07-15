# red, blue, display
# init - display N
# red: N*2
# blue N-1

import sys
#sys.setrecursionlimit(10000)
from functools import lru_cache
n, m = [int(x) for x in input().split()]

# Other direction:
# m++ or m/2, reach n


res = 0
while n < m:
    res += 1
    if m % 2 == 0:
        m //= 2
    else: m += 1

res += (n-m)

print(res)

