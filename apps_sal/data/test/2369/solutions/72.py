N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
fact = [1]
mod = 10**9 + 7
for i in range(1, N + 1):
    fact.append(fact[i - 1] * i % mod)
ifact = [None] * (N + 1)
ifact[N] = pow(fact[N], mod - 2, mod)
for i in range(N, 0, -1):
    ifact[i - 1] = i * ifact[i] % mod


def comb(n, k):
    if n < k:
        return 0
    elif n == 0 or k == 0:
        return 1
    return (fact[n] * ifact[k] * ifact[n - k]) % mod


ans = 0
for i in range(N):
    ans -= comb(N - i - 1, K - 1) * A[i]
    ans += comb(i, K - 1) * A[i]
    ans %= mod
print(ans)
