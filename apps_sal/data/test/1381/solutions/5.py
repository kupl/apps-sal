from math import ceil

k, n, s, p = [int(i) for i in input().split()]
print(ceil(ceil(n / s) * k / p))
