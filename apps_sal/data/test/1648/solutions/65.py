n, k = map(int, input().split())
mod = 10 ** 9 + 7

fact = [1] * (n + 1)
revfact = [1] * (n + 1)
for i in range(n):
    fact[i + 1] = ((i + 1) * fact[i]) % mod
revfact[n] = pow(fact[n], mod - 2, mod)
for i in reversed(range(n)):
    revfact[i] = ((i + 1) * revfact[i + 1]) % mod
def combination(n, k, p):
    return (fact[n] * revfact[k] * revfact[n - k]) % p

for i in range(1, k + 1):
    if n - k + 1 < i:
        ans  = 0
    else:
        ans = combination(n - k + 1, i, mod) * combination(k - 1, i - 1, mod)
    print(ans % mod)
