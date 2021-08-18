def nCr(n, r):
    num, den = 1, 1
    for i in range(n, n - r, -1):
        num = num * i % M
    for i in range(1, r + 1):
        den = den * i % M
    den_inv = pow(den, -1, M)
    return num * den_inv % M


def is_comb():
    a = 1 / 3 * (2 * X - Y)
    b = 1 / 3 * (-X + 2 * Y)
    if a >= 0 and b >= 0 and a.is_integer() and b.is_integer():
        return int(a), int(b)
    return 0, 0


M = 10**9 + 7
X, Y = map(int, input().split())
a, b = is_comb()
if a == b == 0:
    print(0)
else:
    n, r = a + b, a
    print(nCr(n, r))
