r, h = map(int, input().split())
s = h % r
a = (h // r) * 2
if s * s >= 3 * r * r / 4:
    a += 3
elif 2 * s >= r:
    a += 2
else:
    a += 1
print(a)
