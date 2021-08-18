
from fractions import gcd

t, w, b = list(map(int, input().split()))

if w == b:
    print('1/1')
else:
    wb = w * b // gcd(w, b)
    m = min(w, b)
    n = t // wb * m - 1 + min(t % wb + 1, m)
    g = gcd(n, t)
    print("%d/%d" % (n // g, t // g))
