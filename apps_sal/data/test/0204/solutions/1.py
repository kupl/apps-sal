from sys import stdin, stdout


def gcd(a, b):
    if not b:
        return a
    else:
        return gcd(b, a % b)


a, b, x, y = map(int, stdin.readline().split())
g = gcd(x, y)
x //= g
y //= g

l, r = 0, 10 ** 18 + 1
while r - l > 1:
    m = (l + r) >> 1

    if m * x <= a and m * y <= b:
        l = m
    else:
        r = m

stdout.write(str(l))
