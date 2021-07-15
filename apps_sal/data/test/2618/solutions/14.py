from math import gcd


def check(m, a, b, prices, k, x, y):
    acdc = m // a
    bcdc = m // b
    abcdc = m // (a * b // gcd(a, b))
    calc = 0
    while acdc or bcdc:
        new = prices.pop()
        if abcdc:
            calc += new * (x + y) // 100
            abcdc -= 1
            acdc -= 1
            bcdc -= 1
        elif acdc:
            calc += new * x // 100
            acdc -= 1
        else:
            calc += new * y // 100
            bcdc -= 1
    if calc < k:
        return 0
    return 1


n = int(input())
for i in range(n):
    p = int(input())
    prices = list(map(int, input().split()))
    x, a = map(int, input().split())
    y, b = map(int, input().split())
    prices.sort()
    k = int(input())
    L = 0
    R = p
    if y > x:
        x, a, y, b = y, b, x, a
    while R - L > 1:
        m = (R + L) // 2
        if check(m, a, b, prices.copy(), k, x, y):
            R = m
        else:
            L = m
    print(R if check(R, a, b, prices.copy(), k, x, y) else -1)
