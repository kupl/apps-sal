x, k, d = [int(s) for s in input().split()]
x = abs(x)
q, m = divmod(x, d)
if q >= k:
    x -= k * d
else:
    x = m
    if (k - q) & 1:
        x = d - x
print(x)
