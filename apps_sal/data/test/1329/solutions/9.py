from collections import Counter

n = int(input())


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


li = []

for i in range(1, n + 1):
    li += prime_factorize(i)

C = Counter(li)

a, b, c, d, e = 0, 0, 0, 0, 0

for i in C.values():
    if i >= 74:
        e += 1
    elif i >= 24:
        d += 1
    elif i >= 14:
        c += 1
    elif i >= 4:
        b += 1
    elif i >= 2:
        a += 1

point = 0
point += e
point += (d + e) * (a + b + c) + (d + e) * (d + e - 1)
point += (c + d + e) * b + (c + d + e) * (c + d + e - 1)
point += a * ((b + c + d + e) * (b + c + d + e - 1) // 2) + (b + c + d + e) * ((b + c + d + e - 1) * (b + c + d + e - 2) // 2)

print(point)
