from functools import reduce


def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


def gcd_mult(numbers):
    return reduce(gcd, numbers)


def primeFactor(N):
    i, n, ret, d, sq = 2, N, {}, 2, 99
    while i <= sq:
        k = 0
        while n % i == 0:
            n, k, ret[i] = n // i, k + 1, k + 1
        if k > 0 or i == 97:
            sq = int(n**(1 / 2) + 0.5)
        if i < 4:
            i = i * 2 - 1
        else:
            i, d = i + d, d ^ 6
    if n > 1:
        ret[n] = 1
    return ret


def divisors(N):
    pf = primeFactor(N)
    ret = [1]
    for p in pf:
        ret_prev = ret
        ret = []
        for i in range(pf[p] + 1):
            for r in ret_prev:
                ret.append(r * (p ** i))
    return sorted(ret)


N = int(input())
A = [int(a) for a in input().split()]
G = gcd_mult(A)
print(len(divisors(G)))
