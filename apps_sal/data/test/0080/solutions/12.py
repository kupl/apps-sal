import sys


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


(l, r, x, y) = map(int, input().split())
if y % x != 0:
    print(0)
else:
    res = 0
    p = y // x
    t = 1
    while t * t <= p:
        if p % t == 0:
            a = x * t
            b = x * y / a
            if l <= a <= r and l <= b <= r and (gcd(a, b) == x):
                if b != a:
                    res += 2
                else:
                    res += 1
        t += 1
    print(res)
