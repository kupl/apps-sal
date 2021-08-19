mod = 10 ** 9 + 7


def add(a, b):
    return (a + b) % mod


def sub(a, b):
    return (a + mod - b) % mod


def mul(a, b):
    return a % mod * (b % mod) % mod


def power(x, y):
    if y == 0:
        return 1
    elif y == 1:
        return x % mod
    elif y % 2 == 0:
        return power(x, y // 2) ** 2 % mod
    else:
        return power(x, y // 2) ** 2 * x % mod


def div(a, b):
    return mul(a, power(b, mod - 2))


def cc(ii):
    iii = 1
    for ii in range(1, ii + 1):
        iii = iii * ii
    return iii


def cmb(a, b):
    iii = 1
    for ii in range(a - b + 1, a + 1):
        iii = iii * ii % mod
    iiii = 1
    for ii in range(1, b + 1):
        iiii = iiii * ii % mod
    return div(iii, iiii)


(n, k) = list(map(int, input().split()))
ib = k - 1
ir = n - ib
for i in range(1, ib + 2):
    cb = cmb(ib, i - 1)
    cr = cmb(ir, i)
    print(mul(cb, cr))
