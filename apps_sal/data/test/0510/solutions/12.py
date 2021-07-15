a, b, c, d = list(map(int, input().split()))
a, b, c = sorted((a, b, c))
res = 0
if b - a < d:
    res += d - (b - a)
if c - b < d:
    res += d - (c - b)
print(res)

