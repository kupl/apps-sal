from itertools import repeat


def line():
    return list(map(int, input().split()))


def num():
    return int(input())


def gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


q = num()
for _ in repeat(None, q):
    n = num()
    p = sorted(line(), reverse=True)
    x, a = line()
    y, b = line()
    if x > y:
        x, a, y, b = y, b, x, a
    k = num()

    u = lcm(a, b)

    def f(i):
        ums = i // u
        ams, bms = i // a - ums, i // b - ums
        return sum(p[:ums]) * (x + y) + sum(p[ums:ums + bms]) * y + sum(p[ums + bms:ums + bms + ams]) * x

    def cool(e):
        s = 1
        ans = -1
        while s <= e:
            m = (s + e) // 2
            d = f(m)
            if d < k * 100:
                s = m + 1
            else:
                ans = m
                e = m - 1
        return ans

    print(cool(n + 1))
