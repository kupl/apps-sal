import sys
def MI(): return map(int, sys.stdin.readline().rstrip().split())


N, K = MI()
mod = 10**9 + 7


def divisor(n):  # nの約数のリスト
    res = []
    for i in range(1, int(n**.5) + 1):
        if n % i == 0:
            res.append(i)
            if i != n // i:
                res.append(n // i)
    return res


A = divisor(N)

d = {}  # d[i] = iの約数のリスト(iはNの約数)
for a in A:
    d[a] = divisor(a)

prime = []  # Nの素因数のリスト
for i in range(2, int(N**.5) + 1):
    if N % i == 0:
        prime.append(i)
        while N % i == 0:
            N //= i
if N != 1:
    prime.append(N)

mu = {}  # mu[i] = μ(i) (iはNの約数)
for a in A:
    b = a
    r = 1
    for p in prime:
        if b % p == 0:
            r *= -1
            if b // p % p == 0:
                r = 0
                break
    mu[a] = r


ans = 0
for a in A:
    for b in d[a]:
        if a % 2 == 0:
            ans += mu[a // b] * pow(K, (b + 1) // 2, mod) * (a // 2)
            ans %= mod
        else:
            ans += mu[a // b] * pow(K, (b + 1) // 2, mod) * a
            ans %= mod

print(ans)
