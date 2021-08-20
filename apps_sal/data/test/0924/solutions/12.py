import sys
import math
inp = iter(map(int, sys.stdin.read().split()))
la = next(inp)
ra = next(inp)
ta = next(inp)
lb = next(inp)
rb = next(inp)
tb = next(inp)
if la > lb:
    (la, lb) = (lb, la)
    (ra, rb) = (rb, ra)
    (ta, tb) = (tb, ta)


def area(l1, r1, l2, r2):
    l = max(l1, l2)
    r = min(r1, r2)
    return r - l + 1


d = lb - la
g = math.gcd(ta, tb)
shift = d // g * g
ans = 0
for d in range(-100, 101):
    ans = max(ans, area(la, ra, lb - shift - g * d, rb - shift - g * d))
print(ans)
