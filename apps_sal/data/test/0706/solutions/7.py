MOD = 10 ** 9 + 7


def pow(a, n):
    res = 1
    b = a
    while n != 0:
        if n % 2:
            res = (res * b) % MOD
        n //= 2
        b = (b * b) % MOD
    return res


assert pow(2, 10) == 1024
assert pow(7, 1) == 7
assert pow(7, 0) == 1


def egcd(a, b):
    assert a > 0 and b > 0

    a_orig = a
    b_orig = b

    x0, y0 = 1, 0
    x1, y1 = 0, 1

    assert a == a_orig * x0 + b_orig * y0
    assert b == a_orig * x1 + b_orig * y1

    while b != 0:
        q = a // b

        a, b = b, a - b * q
        x0, y0, x1, y1 = x1, y1, x0 - q * x1, y0 - q * y1

        assert a == a_orig * x0 + b_orig * y0
        assert b == a_orig * x1 + b_orig * y1

    return a, x0, y0


if False:
    print(egcd(3, 5))
    print(egcd(2, 4))
    print(egcd(4, 2))
    print(egcd(5, 3))


def solve(a, b, n, x):
    if a == 1:
        return (x + b * n) % MOD

    a_n = pow(a, n)
    one, inv_a_1, _ = egcd(a - 1, MOD)
    assert one == 1
    assert ((a - 1) * inv_a_1) % MOD == 1
    res = (a_n * x + b * (a_n - 1) * inv_a_1) % MOD

    return res


if False:
    assert solve(3, 4, 2, 1) == 25
    assert solve(3, 4, 1, 1) == 7
    solve(10 ** 9 - 19, 10 ** 9 - 23, 10 ** 18 - 57, 10 ** 9 - 16)
    assert solve(1, 4, 2, 10) == 18

else:
    a, b, n, x = list(map(int, input().split()))
    print(solve(a, b, n, x))
