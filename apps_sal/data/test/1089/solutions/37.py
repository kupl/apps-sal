(N, M, K) = list(map(int, input().split()))


def cmb(n, r, p):
    if r < 0 or n < r:
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % p


p = 10 ** 9 + 7
mod = 10 ** 9 + 7
n = 3 * 10 ** 5
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
for i in range(2, n + 1):
    fact.append(fact[-1] * i % p)
    inv.append(-inv[p % i] * (p // i) % p)
    factinv.append(factinv[-1] * inv[-1] % p)
ans1 = 0
for i in range(1, M):
    ans1 += i * (M - i) % mod
ans1 = ans1 * N * N % mod
ans2 = 0
for i in range(1, N):
    ans2 += i * (N - i) % mod
ans2 = ans2 * M * M % mod
ans = ans1 + ans2
print(ans * cmb(M * N - 2, K - 2, p) % mod)
