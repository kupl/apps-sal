inp = input()
n, m, k = [int(x) for x in inp.split()]


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


if 2 * n * m % k != 0:
    print('NO')
else:
    print('YES')
    if n * m % k != 0:
        k //= 2
        need = False
    else:
        need = True
    p = gcd(n, k)
    q = k // p
    x = n // p
    y = m // q
    if need:
        if p > 1:
            x *= 2
        else:
            y *= 2
    print(0, 0)
    print(x, 0)
    print(0, y)
