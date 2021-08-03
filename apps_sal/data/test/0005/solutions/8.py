import itertools as it
import math
import functools as ft
n, pos, l, r = map(int, input().split())
res = 0
if l == 1:
    if r == n:
        res = 0
    else:
        res = abs(pos - r) + 1
else:
    if r == n:
        res = abs(pos - l) + 1
    else:
        xl = abs(pos - l)
        xr = abs(r - pos)
        if xl <= xr:
            res = xl + 1
            if l > 1:
                res += (r - l) + 1
        else:
            res = xr + 1
            if r < n:
                res += (r - l) + 1

print(res)
