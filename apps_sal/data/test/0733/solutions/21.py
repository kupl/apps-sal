# -*- coding: utf-8 -*-

def gcd(a, b):
    x, y = max(a, b), min(a, b)
    while x % y:
        x, y = y, x % y
    return y


def test():
    assert gcd(1071, 462) == 21
    assert gcd(462, 1071) == 21
    assert gcd(81, 135) == 27
    print("test passes")


def solve(x, y, a, b):
    tmp = x * y // gcd(x, y)
    #print(x, y, gcd(x, y))
    #print(b // tmp, a // tmp)
    return b // tmp - (a - 1) // tmp


x, y, a, b = list(map(int, input().split()))
print(solve(x, y, a, b))
