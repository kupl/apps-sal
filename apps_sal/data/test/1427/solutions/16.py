import math
from functools import reduce
from collections import defaultdict

#素因数分解O(√n)
def primeFactor(n):
    res = defaultdict(lambda: 0)
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            res[i] += 1
            n = n // i
    if n != 1:
        res[n] += 1
    return res

    

N = int(input())
A = list(map(int, input().split()))

def gcd(*numbers):
    return reduce(math.gcd, numbers)

MOD = 10**9+7
GCD = gcd(*A)

P = defaultdict(lambda: 0)

for i in range(N):
    factors = primeFactor(A[i])
    for k, v in list(factors.items()):
        if v > P[k]:
            P[k] = v


P_mod = 1
for k in list(P.keys()):
    P_mod = P_mod*(k**P[k])%MOD

ans = 0
for i in range(N):
    b = A[i]
    mod_inv = pow(b, MOD-2, MOD)
    ans = (ans + P_mod * mod_inv) % MOD

print(ans)



