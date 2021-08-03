def check(t):
    if x == int(x):
        return True
    else:
        return False


def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)


a, b, c, d = list(map(int, input().split()))
a *= max(c, d)
b *= max(c, d)
r = c / d
if a / b < r:
    x = b * c - a * d
    b = b * c

    u = gcd(x, b)
    p = str(int(x / u)) + '/' + str(int(b / u))
    print(p)

else:
    x = a * d - c * b
    a = a * d

    u = gcd(x, a)
    p = str(int(x / u)) + '/' + str(int(a / u))
    print(p)
