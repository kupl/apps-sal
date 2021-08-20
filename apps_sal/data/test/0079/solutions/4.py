from math import floor
from functools import reduce
MOD = floor(1000000000.0 + 7)
expected_len = [0, 1]
n = int(input())
factors = [[] for i in range(n + 1)]
prime_factors = [[] for i in range(n + 1)]


def ext_euclid(a, b):
    if b == 0:
        return (1, 0, a)
    (x, y, q) = ext_euclid(b, a % b)
    (x, y) = (y, x - a // b * y)
    return (x, y, q)


def inverse(num):
    return ext_euclid(MOD, num)[1] % MOD


inv = [0] * (n + 1)
for i in range(n + 1):
    inv[i] = inverse(i)
for i in range(1, n + 1):
    prime_fact = False
    if len(prime_factors[i]) < 2:
        prime_factors[i].append(i)
        prime_fact = True
    factors[i].append(i)
    for j in range(2 * i, n + 1, i):
        factors[j].append(i)
        if prime_fact:
            prime_factors[j].append(i)


def f(x, y):
    remain = 0
    new_n = n // x
    new_y = reduce(lambda x, y: x * y, prime_factors[y])
    for fact in factors[new_y]:
        if fact != 1:
            if len(prime_factors[fact]) & 1:
                remain -= new_n // fact
            else:
                remain += new_n // fact
    return new_n - remain


for i in range(2, n + 1):
    e_len = 0
    for ele in factors[i]:
        if ele != i:
            e_len += f(ele, i // ele) * expected_len[ele] * inv[n] % MOD
    e_len = (e_len + 1) * n * inv[n - f(i, 1)] % MOD
    expected_len.append(e_len)
print(sum(expected_len) * inv[n] % MOD)
