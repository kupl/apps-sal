#!/usr/bin/env python3
N = int(input())

MOD = 1000000007
cache = {0: 1, 1: 2}


def f(n):
    if n in cache:
        return cache[n]
    if n % 2 == 0:
        result = 2 * f(n // 2 - 1) + f(n // 2)
    else:
        result = f(n // 2 - 1) + 2 * f(n // 2)
    result %= MOD
    cache[n] = result
    return result


print((f(N)))

