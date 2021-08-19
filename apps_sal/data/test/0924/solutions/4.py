from math import gcd


def inters(x1, y1, x2, y2):
    return max(0, min(y1, y2) - max(x1, x2) + 1)


(la, ra, ta) = list(map(int, input().split()))
(lb, rb, tb) = list(map(int, input().split()))
shift = gcd(ta, tb)
start = la - la % shift
la -= start
ra -= start
start = lb - lb % shift
lb -= start
rb -= start
res = max(inters(la, ra, lb + shift, rb + shift), inters(la + shift, ra + shift, lb, rb), inters(la, ra, lb, rb))
print(res)
