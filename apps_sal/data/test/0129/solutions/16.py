import math

n, m, k, l = map(int, input().split())

x = (l + k) // m
if x * m < l + k:
    x += 1
assert x * m >= l + k

if m * x > n:
    print(-1)
else:
    print(x)
