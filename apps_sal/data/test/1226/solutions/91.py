ip = input().split(' ')
n = int(ip[0])
a = int(ip[1])
b = int(ip[2])
m = 1000000007


def modMul(a, b, mod):
    return a * b % mod


def fastExp(b, exp, mod):
    res = 1
    base = b
    while exp > 0:
        if exp % 2 == 1:
            res = modMul(res, base, mod)
        base = modMul(base, base, mod)
        exp >>= 1
    return res


def getncr(n, r, m):
    num = 1
    fact = 1
    for i in range(r):
        num = modMul(num, n - i, m)
        fact = modMul(i + 1, fact, m)
    return modMul(num, fastExp(fact, m - 2, m), m)


def solve(n, a, b, m):
    got = fastExp(2, n, m) - 1
    for_a = getncr(n, a, m)
    for_b = getncr(n, b, m)
    got -= for_a
    if got < 0:
        got += m
    got -= for_b
    if got < 0:
        got += m
    print(got)


solve(n, a, b, m)
