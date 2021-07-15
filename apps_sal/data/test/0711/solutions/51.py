P = 10**9 + 7

def modpow(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return (modpow(a, n // 2)**2) % P
    else:
        return (a * modpow(a, n // 2)**2) % P

def inv(a):
    return modpow(a, P - 2)

fac = [1]*(2*10**5)
for i in range(1, 2*10**5):
    fac[i] = (i * fac[i - 1]) % P

primes = []
check = [False]*10**5
for p in range(2, 10**5):
    if check[p]:
        continue
    primes.append(p)
    for j in range((10**5 - 1) // p + 1):
        check[p * j] = True

def pf(M):
    ans = {}
    for p in primes:
        e = 0
        while M % p == 0:
            M //= p
            e += 1
        if e > 0:
            ans[p] = e
    if M > 1:
        ans[M] = 1
    return ans

N, M = map(int, input().split())
pfM = pf(M)

ans = 1
for p in pfM:
    e = pfM[p]
    dup = (fac[e + N - 1] * inv(fac[e]) * inv(fac[N - 1])) % P
    ans = (ans * dup) % P
print(ans)
