from math import ceil

k, n, s, p = list(map(int, input().split()))

print(ceil(k * ceil(n / s) / p))
