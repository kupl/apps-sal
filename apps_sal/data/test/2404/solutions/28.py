n = int(input())


def SieveOfEratosthenes(n):

    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):

        if (prime[p] == True):

            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    res = []
    for p in range(n + 1):
        if prime[p]:
            res.append(p)

    return res


primes = SieveOfEratosthenes(1000)
pset = set(primes)


m1 = None
m2 = None
for p in primes:
    if n % p == 0:
        e = n // p
        if e in pset:
            m1, m2 = p, e
            break

res = ''
if m1 is not None and m2 is not None:
    if m1 > m2:
        m1, m2 = m2, m1

    res += str(m1) + str(m2)

print(res)
