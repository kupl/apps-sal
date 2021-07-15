import numpy as np

def divisors(N):
    return sorted(sum((list({n, N // n}) for n in range(1, int(N ** 0.5) + 1) if not N % n), []))

def prime_factorize_dict(n):
    d = dict()
    while not n & 1:
        d[2] = d.get(2, 0) + 1
        n >>= 1
    f = 3
    while f * f <= n:
        if not n % f:
            d[f] = d.get(f, 0) + 1
            n //= f
        else:
            f += 2
    if n != 1:
        d[n] = d.get(n, 0) + 1
    return d

N = int(input())
count = 0
for n in divisors(N)[1:]:
    M = N
    while not M % n:
        M //= n
    count += M % n == 1
fact_Nm1 = np.array(list(prime_factorize_dict(N - 1).values()), dtype=np.int32)
print(count + np.prod(fact_Nm1 + 1) - 1)
