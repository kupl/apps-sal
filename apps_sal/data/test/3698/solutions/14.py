# python3
import sys
from functools import lru_cache

sys.setrecursionlimit(1000000)

MOD = int(1e+9 + 7)


def inv(val): return pow(val, MOD - 2, MOD)


@lru_cache(maxsize=None)
def factorial(n):
    return 1 if n < 2 else (factorial(n - 1) * n % MOD)


def choose(n, k):
    return factorial(n) * inv(factorial(k) * factorial(n-k)) % MOD


def numbers_with_bits(length, n):
    nxt = 0
    res = 0
    while nxt != -1 and length > 0:
        top = len(n) - 1 - nxt

        if(length <= top):
            res += choose(top, length)
            res %= MOD

        nxt = n.find('1', nxt + 1)
        length -= 1

    if length == 0:
        res += 1

    return res


def bits(n): return bin(n).count('1')


def solve(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return len(n) - 1  # exclude the 1
    elif k > 5:
        return 0

    ans = 0
    f = [-1, 0]
    for i in range(2, 1001):
        f.append(f[bits(i)] + 1)
        if f[i] == k - 1:
            ans += numbers_with_bits(i, n)
            ans %= MOD
    return ans

print(solve(n=input(), k=int(input())))

