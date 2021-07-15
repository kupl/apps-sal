from collections import Counter  # N : 素因数分解

MOD = 10**9 + 7


def comb(n, r):
    r = r if n-r <= r else n-r
    a = 1
    for x in list(range(r + 1, n + 1)):
        a *= x % MOD
    b = 1
    for x in list(range(1, n - r + 1)):
        b *= x % MOD
    return (a // b)


N, M = [int(s) for s in input().split()]
prime_factor = []
for i in range(2,int(M**0.5)+1):
    while M%i == 0:
        prime_factor.append(i)
        M/=i
if M > 1:
    prime_factor.append(M)
    
c = Counter(prime_factor)

result = 1

for b in list(c.values()):
    result *= comb(b+N-1, b) % MOD


print((result % MOD))

