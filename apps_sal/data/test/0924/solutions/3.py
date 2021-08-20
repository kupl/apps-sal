from math import gcd
(la, ra, ta) = list(map(int, input().split()))
(lb, rb, tb) = list(map(int, input().split()))
g = gcd(ta, tb)
ra -= la
temp = rb - lb
lb -= la
lb %= g
rb = lb + temp
current = min(rb, ra) - lb + 1
now = min(rb, ra + g) - g + 1
print(max(current, now, 0))
