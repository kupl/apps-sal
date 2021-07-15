from math import ceil
h, m = list(map(int, input().split()))
H, d, c, n = list(map(float, input().split()))
if h >= 20:
    print(round(ceil(H / n) * c * 0.8, 3))
else:
    print(round(min(ceil(H / n) * c, ceil(((20 * 60 - h * 60 - m) * d + H) / n) * c * 0.8), 3))

