def lcm(a, b):
    x = a * b
    while b != 0:
        (a, b) = (b, a % b)
    return x // a


n, a, b, p, q = map(int, input().split())
print(n // a * p + n // b * q - n // lcm(a, b) * min(p, q))
