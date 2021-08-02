import sys
import math


def solve():
    n = int(input())
    l, r = -float('inf'), float('inf')
    for line in sys.stdin:
        c, d = list(map(int, line.split()))
        if d == 1:
            l = max(1900, l)
        else:
            r = min(1899, r)
        l += c
        r += c

    if r < l:
        return None
    else:
        return r


res = solve()
if res is None:
    print('Impossible')
elif math.isinf(res):
    print('Infinity')
else:
    print(res)
