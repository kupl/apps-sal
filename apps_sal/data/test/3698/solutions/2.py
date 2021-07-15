from math import factorial
from functools import lru_cache

mod = 1000000007

def num_iters(x):
    ans = 0
    while x > 1:
        x = bin(x).count('1')
        ans += 1
    return ans

@lru_cache(maxsize=1001)
def fact(n):
    return factorial(n) % mod

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

@lru_cache(maxsize=1001)
def inv(a):
    return modinv(a, mod)

def binom(n, k):
    return (fact(n) * inv(fact(k)) * inv(fact(n - k))) % mod

def num_numbers(n, i):
    # number of numbers in [1..n] that have exactly i 1s
    # in their binary representation
    # n is a str

    ans = 0
    num_ones_in_prefix = 0
    for j in range(len(n) - 1):
        pos_right = len(n) - j - 1
        if num_ones_in_prefix + pos_right < i or num_ones_in_prefix > i:
            break
        if n[j] == '1':
            ans = (ans + binom(pos_right, i - num_ones_in_prefix)) % mod
            num_ones_in_prefix += 1

    cnt1 = n.count('1')
    if (n[-1] == '0' and cnt1 == i) or (n[-1] == '1' and cnt1 in (i, i + 1)):
        ans = (ans + 1) % mod

    return ans

precalc = [num_iters(x) for x in range(1001)]

def solve(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return len(n) - 1
    else:
        ans = 0
        for i in range(1, 1001):
            if precalc[i] == k - 1:
                ans = (ans + num_numbers(n, i)) % mod
        return ans

n = input()
k = int(input())

print(solve(n, k))

