def f(): return map(int, input().split())


a, b = f()
c, d = f()


def g(p, k):
    s = 1
    while k % p ** s == 0:
        s += 1
    return s - 1


a3, b3, c3, d3 = g(3, a), g(3, b), g(3, c), g(3, d)
a2, b2, c2, d2 = g(2, a), g(2, b), g(2, c), g(2, d)

ab3, cd3 = a3 + b3, c3 + d3
ab2, cd2 = a2 + b2, c2 + d2

ab = a * b * pow(2, cd2) * pow(3, cd3)
cd = c * d * pow(2, ab2) * pow(3, ab3)
if ab != cd:
    print(-1)
    return

k, s2, s3 = 1e9, 0, 0

for t3 in range(min(ab3, cd3) + 1):
    k3 = ab3 + cd3 - 2 * t3
    for t2 in range(min(ab2 + ab3, cd2 + cd3) - t3 + 1):
        k2 = k3 + ab2 + cd2 - 2 * t2

        if k2 + k3 < k:
            k = k2 + k3
            s2, s3 = t2, t3

t3 = ab3 - s3
while t3 and a % 3 == 0:
    a = 2 * a // 3
    t3 -= 1
while t3 and b % 3 == 0:
    b = 2 * b // 3
    t3 -= 1
t2 = ab3 - s3 + ab2 - s2
while t2 and a % 2 == 0:
    a = a // 2
    t2 -= 1
while t2 and b % 2 == 0:
    b = b // 2
    t2 -= 1
t3 = cd3 - s3
while t3 and c % 3 == 0:
    c = 2 * c // 3
    t3 -= 1
while t3 and d % 3 == 0:
    d = 2 * d // 3
    t3 -= 1
t2 = cd3 - s3 + cd2 - s2
while t2 and c % 2 == 0:
    c = c // 2
    t2 -= 1
while t2 and d % 2 == 0:
    d = d // 2
    t2 -= 1

print(k)
print(a, b)
print(c, d)
