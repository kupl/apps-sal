A, B = [int(x) for x in input().split()]


def prime_factorization(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


Aprimes = prime_factorization(A)
Bprimes = set(prime_factorization(B))

ans = 1
ansset = set()
for a in Aprimes:
    if a in ansset:
        continue
    if a in Bprimes:
        ansset.add(a)
        ans += 1

print(ans)
