import math
r, h = map(int, input().split())
a = h // r * 2
if 2 * (h % r) >= math.sqrt(3) * r:
    a += 3
elif 2 * (h % r) >= r:
    a += 2
else:
    a += 1
print(a)
