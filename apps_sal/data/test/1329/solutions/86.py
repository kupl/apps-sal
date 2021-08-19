import numpy as np


def prime_factorize(N):
    exponent = 0
    while N % 2 == 0:
        exponent += 1
        N //= 2
    if exponent:
        factorization = [[2, exponent]]
    else:
        factorization = []
    i = 1
    while i * i <= N:
        i += 2
        if N % i:
            continue
        exponent = 0
        while N % i == 0:
            exponent += 1
            N //= i
        factorization.append([i, exponent])
    if N != 1:
        factorization.append([N, 1])
    assert N != 0, 'zero'
    return factorization


factors = [0] * 100
N = int(input())
for i in range(1, N + 1):
    for (p, n) in prime_factorize(i):
        factors[p] += n
factors = np.array(factors)
ov2 = len(factors[factors >= 2])
ov4 = len(factors[factors >= 4])
ov14 = len(factors[factors >= 14])
ov24 = len(factors[factors >= 24])
ov74 = len(factors[factors >= 74])
ans = 0
ans += (ov4 - 2) * ov4 * (ov4 - 1) // 2 + (ov2 - ov4) * ov4 * (ov4 - 1) // 2
ans += (ov4 - ov14) * ov14 + ov14 * (ov14 - 1)
ans += (ov2 - ov24) * ov24 + ov24 * (ov24 - 1)
ans += ov74
print(ans)
