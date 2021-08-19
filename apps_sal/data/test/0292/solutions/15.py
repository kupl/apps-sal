(h, n) = list(map(int, input().split()))
z = 2
z1 = 1
p = 0
r = 0
h2 = 0
h3 = 2 ** h
while p < h:
    if n <= h2 + h3 // z and r == 0:
        z1 += 1
        z *= 2
        r = 1
    elif n > h2 + h3 // z and r == 0:
        h2 += h3 // z
        z1 += 2 ** (h - p)
        z *= 2
        r = 0
    elif n <= h2 + h3 // z and r == 1:
        z1 += 2 ** (h - p)
        z *= 2
        r = 1
    elif n > h2 + h3 // z and r == 1:
        h2 += h3 // z
        z1 += 1
        z *= 2
        r = 0
    p += 1
print(z1 - 1)
