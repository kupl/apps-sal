from math import ceil
(k, d, t) = list(map(int, input().split()))
d = ceil(k / d) * d
(r, t) = divmod(t, k + (d - k) * 0.5)
print(r * d + min(k, t) + max(t - k, 0) * 2)
