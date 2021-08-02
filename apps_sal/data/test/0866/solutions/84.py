X, Y = map(int, input().split())


def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


p = 10 ** 9 + 7
N = 10 ** 6
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

if (X + Y) % 3:
    ans = 0
else:
    N = (X + Y) // 3
    if N <= X <= 2 * N and N <= Y <= 2 * N:
        ans = cmb(N, X - N, p)
    else:
        ans = 0

print(ans)
