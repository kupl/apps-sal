
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def main():
    L, a, b = list(map(int, input().split()))
    c = a // gcd(a, b) * b
    m = min(a, b)
    if c <= m:
        print('1/1')
    else:
        p = L // c * m
        p += min(L % c, m - 1)
        g = gcd(p, L)
        print('%d/%d' % (p // g, L // g))


main()
