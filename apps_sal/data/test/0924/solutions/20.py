from math import gcd


def r(): return list(map(int, input().split()))


a, b = r(), r()
c = b[0] > a[0]
la, ra, ta = a if c else b
lb, rb, tb = b if c else a

g = gcd(ta, tb)
lna, lnb = ra - la + 1, rb - lb + 1
d = lb - la - (lb - la) // g * g
print(max(0, min(lna - d, lnb), min(lna, lnb - g + d)))
