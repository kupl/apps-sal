n, a, b = [int(x) for x in input().split()]


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


g, a_1, b_1 = egcd(a, b)
if n % g:
    print(-1)
    return

fac = n // g
a_1 *= fac
b_1 *= fac
if a_1 < 0:
    while a_1 < 0:
        a_1 += b // g
        b_1 -= a // g
    if b_1 < 0:
        print(-1)
        return
elif b_1 < 0:
    while b_1 < 0:
        b_1 += a // g
        a_1 -= b // g
    if a_1 < 0:
        print(-1)
        return

res = []
i = 1
for _ in range(a_1):
    for j in range(a - 1):
        i += 1
        res.append(i)
    res.append(i - a + 1)
    i += 1

for _ in range(b_1):
    for j in range(b - 1):
        i += 1
        res.append(i)
    res.append(i - b + 1)
    i += 1

print(" ".join(map(str, res)))
