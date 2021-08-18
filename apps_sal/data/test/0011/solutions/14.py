def cin(): return map(int, input().split())


n, a, b, p, q = cin()


def lcm(a, b):
    m = a * b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a + b)


if p >= q:
    res = (n // a) * p + (n // b - n // lcm(a, b)) * q
else:
    res = (n // b) * q + (n // a - n // lcm(a, b)) * p
print(res)
