from math import ceil
k, n, s, p = [int(i)for i in input().split()]
x = ceil(n / s)
print(ceil((x * k) / p))
