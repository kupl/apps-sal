from math import ceil

k, n, s, p = map(int, input().split())

l = ceil(n / s)

t = int(ceil(k * l / p))

print(t)
