r1, c1, r2, c2 = list(map(int, input().split()))

mod = 1000000007

# return an integer k s.t. (a * k) % p = 1 and 0 <= k < p.


def inversion(a):
    b = mod
    u, v = 1, 0
    while b >= 1:
        t = a // b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    u %= mod
    if u < 0:
        u += mod
    return u


fact = [0 for i in range(2000003)]
for i in range(2000003):
    if i <= 1:
        fact[i] = 1
    else:
        fact[i] = (fact[i - 1] * i) % mod

# return nCr % p.


def combination(n, r):
    return (((fact[n] * inversion(fact[r])) % mod) * inversion(fact[n - r])) % mod


answer = (
    combination(r2 + c2 + 2, r2 + 1)
- combination(r2 + c1 + 1, r2 + 1)
- combination(r1 + c2 + 1, c2 + 1)
    + combination(r1 + c1, c1) )

answer %= mod

if answer < 0:
    answer += mod

print(answer)
