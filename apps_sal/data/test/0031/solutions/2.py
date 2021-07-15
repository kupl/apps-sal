#!/usr/bin/env python3
import os
MOD = 1000003
inv2 = pow(2, MOD - 2, MOD)

def logm(n, m):
    # log = 3.3
    # return (3, False)
    ans = 0
    whole = True
    while n >= m:
        whole = whole and (n % m == 0)
        ans += 1
        n //= m
    if n == 1:
        return (ans, whole)
    return (ans, False)



def fact_exp(n, k):
    ans = 0
    while n != 0:
        n //= k
        ans += n
    return ans


def main():
    n, k = list(map(int, input().split()))
    e2 = n + fact_exp(k - 1, 2)
    div = pow(2, n * k - e2, MOD)

    (e, w) = logm(k, 2)
    if e > n or (e == n and not w):
        print(1, 1)
        return

    num = 1
    Nr = pow(2, n, MOD)
    # N * (N-1) * ... * (N - k + 1)
    # (-0) * (-1) * 
    for t in range(1, k):
        i = (Nr - t) % MOD
        if i == 0:
            num = 0
            break

        p = 0
        while t % 2 == 0:
            p += 1
            t //= 2

        num = num * i * pow(inv2, p, MOD) % MOD

    print((div - num) % MOD, div)

def __starting_point():
    main()

__starting_point()
