import math
N, M = map(int, input().split())


def prime_fac(n):
    p_lis = []
    temp = n

    for i in range(2, int(math.sqrt(n)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            p_lis.append([i, cnt])
    if temp != 1:
        p_lis.append([temp, 1])
    if p_lis == []:
        p_lis.append([n, 1])

    return p_lis


mod = 10 ** 9 + 7
MAX = 10 ** 6
fac = [1, 1]
finv = [1, 1]
inv = [0, 1]


def comb(n, r):
    if n < r:
        return 0
    else:
        return fac[n] * (finv[r] * finv[n - r] % mod) % mod


for i in range(2, MAX + 1):
    fac.append((fac[-1] * i) % mod)
    inv.append(mod - (inv[mod % i] * (mod // i) % mod))
    finv.append(finv[-1] * inv[-1] % mod)

ans = 1

for p, a in prime_fac(M):
    if a == p == 1:
        break
    ans *= comb(N + a - 1, a)
    ans %= mod

print(ans)
