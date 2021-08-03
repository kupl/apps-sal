t = int(input())


def ext_gcd(p, q):
    # p * x + q * y = gcd(p,q) = g となる整数(x, y, g)を求める
    if q == 0:
        return (p, 1, 0)
    g, y, x = ext_gcd(q, p % q)
    y -= (p // q) * x
    return (g, x, y)


for _ in range(t):
    r, b, k = map(int, input().split())
    ponta = ext_gcd(r, b)[0]
    if ponta <= b - 1 - (k - 1) * r or ponta <= r - 1 - (k - 1) * b:
        print("REBEL")
    else:
        print("OBEY")
