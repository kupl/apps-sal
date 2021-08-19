(a, b, c) = list(map(int, input().split()))
md = 998244353


def solve(x, y, z):
    res1 = 0
    res2 = 0
    res3 = 0
    (a, b, c) = sorted([x, y, z])
    (tmpA, tmpB, tmpC, tmpK) = (1, 1, 1, 1)
    for k in range(a + 1):
        d = pow(tmpK, md - 2, md)
        res1 += tmpA * tmpB * d % md
        res2 += tmpA * tmpC * d % md
        tmpA *= a - k
        tmpA %= md
        tmpB *= b - k
        tmpB %= md
        tmpC *= c - k
        tmpC %= md
        tmpK *= k + 1
        tmpK %= md
        res1 = res1 % md
        res2 = res2 % md
    (tmpB, tmpC, tmpK) = (1, 1, 1)
    for k in range(b + 1):
        d = pow(tmpK, md - 2, md)
        res3 += tmpB * tmpC * d % md
        tmpB *= b - k
        tmpB %= md
        tmpC *= c - k
        tmpC %= md
        tmpK *= k + 1
        tmpK %= md
        res3 = res3 % md
    return res1 * res2 * res3 % md


res = solve(a, b, c) % 998244353
print(res)
