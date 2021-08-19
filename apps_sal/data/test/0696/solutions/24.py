p = int(input())


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


c = 0
for i in range(1, p):
    if gcd(p - 1, i) == 1:
        c += 1
print(c)
