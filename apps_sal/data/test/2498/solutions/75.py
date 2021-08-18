def gcd(a, b):
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)


def lcm(a, b):
    x = gcd(a, b)
    return a * b // x


def gcdN(a):
    x = a[0]
    for i in range(1, len(a)):
        x = gcd(x, a[i])
    return x


def lcmN(a):
    x = a[0]
    for i in range(1, len(a)):
        x = lcm(x, a[i])
    return x


n, m = list(map(int, input().split()))
a = list(map(int, input().split()))

g = gcdN(a)
for i in a:
    if (i // g) % 2 == 0:
        print((0))
        break
else:
    l = lcmN(a)
    k = 2 * m // l
    print(((k + 1) // 2))
