import math


def R():
    return list(map(int, input().split()))


(hh, mm) = R()
(h, d, c, n) = R()
cb = math.ceil(h * 1.0 / n) * c
mn = hh * 60 + mm
e = 20 * 60
dp = c * 0.8
if mn <= e:
    nh = h + d * (e - mn)
    cb = min(cb, math.ceil(nh * 1.0 / n) * dp)
else:
    cb = cb * 0.8
print(cb)
