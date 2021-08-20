from math import ceil
(h, m) = map(int, input().split())
(k, d, c, n) = map(int, input().split())
if h >= 20:
    print(ceil(k / n) * (c * 0.8))
else:
    a1 = ceil(k / n) * c
    r = 60 * (20 - h) - m
    a2 = ceil((k + r * d) / n) * (c * 0.8)
    print(min(a1, a2))
