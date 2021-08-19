def gcd(x, y):
    while x != 0:
        (x, y) = (y % x, x)
    return y


def main():
    (a, b, c, d) = [int(item) for item in input().split()]
    k1 = float(a) / float(b)
    k2 = float(c) / float(d)
    p = 0
    q = 1
    g = 0
    if k1 > k2:
        q = a * d
        p = q - b * c
        g = gcd(p, q)
    elif k1 < k2:
        q = b * c
        p = q - a * d
        g = gcd(p, q)
    if g > 1:
        p = int(p / g)
        q = int(q / g)
    print('{}/{}'.format(p, q))


main()
