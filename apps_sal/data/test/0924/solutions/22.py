from math import gcd

la, ra, ta = list(map(int, input().split()))
lb, rb, tb = list(map(int, input().split()))
k = gcd(ta, tb)
d1 = (la - lb)
d1 %= k
if d1 < 0:
    d1 += k
d2 = (lb - la)
d2 %= k
if d2 < 0:
    d2 += k
la = ra - la + 1
lb = rb - lb + 1
ans = max(0, min(la - d2, lb), min(la, lb - d1))
print(ans)
