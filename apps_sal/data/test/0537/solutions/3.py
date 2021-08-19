from math import floor
(n, k) = list(map(int, input().split()))
r = floor(n / (2 * (k + 1)))
print(r, k * r, n - r * (k + 1))
