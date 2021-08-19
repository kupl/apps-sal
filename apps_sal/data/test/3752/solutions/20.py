import math
(k, d, t) = map(int, input().split())
l = math.ceil(k / d) * d - k
m = 2 * t // (2 * k + l)
if t - m * (k + l / 2) <= k:
    print(m * (k + l) + t - m * (k + l / 2))
else:
    print(m * (l + k) + k + 2 * (t - m * (k + l / 2) - k))
