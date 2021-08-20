(h, w, a, b) = map(int, input().split())
MOD = 10 ** 9 + 7
N = h + w + 10
fact = [0 for _ in range(N)]
invfact = [0 for _ in range(N)]
fact[0] = 1
for i in range(1, N):
    fact[i] = fact[i - 1] * i % MOD
invfact[N - 1] = pow(fact[N - 1], MOD - 2, MOD)
for i in range(N - 2, -1, -1):
    invfact[i] = invfact[i + 1] * (i + 1) % MOD


def nCk(n, k):
    if k < 0 or n < k:
        return 0
    else:
        return fact[n] * invfact[k] * invfact[n - k] % MOD


ans = 0
a += 1
b += 1
n = h - a + b - 1
n2 = w - b + a - 1
while a <= h and b <= w:
    ans += nCk(n, b - 1) * nCk(n2, w - b)
    ans %= MOD
    a += 1
    b += 1
print(ans)
