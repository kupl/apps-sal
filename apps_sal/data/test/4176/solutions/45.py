def gcd(m, n):
    if m < n:
        m, n = n, m

    while True:
        r = m % n
        if r == 0:
            return n
        else:
            m, n = n, r


def lcm(m, n):
    return m * n // gcd(m, n)


a, b = list(map(int, input().split()))

print((lcm(a, b)))
