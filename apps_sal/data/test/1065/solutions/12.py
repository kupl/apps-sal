from math import floor
(n, k, M, D) = map(int, input().split())
_max = M
for g in range(2, D + 1):
    x = min(M, n // ((g - 1) * k + 1))
    max_g = g * x
    _max = max(_max, max_g)
print(_max)
