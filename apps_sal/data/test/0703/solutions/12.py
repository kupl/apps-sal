from math import ceil

k, a, b, v = list(map(int, input().split()))

res = 0
c = ceil(a / v)
while (b >= k - 1) and (c > 0):
    res += 1
    c -= k
    b -= k - 1

if c > 0:
    res += 1
    c -= b + 1

if c > 0:
    res += c

print(res)

