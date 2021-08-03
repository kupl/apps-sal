n, k = list(map(int, input().split()))
alst = list(map(int, input().split()))

MOD = 10 ** 9 + 7
N = n + 10
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


alst.sort()
ans = 0
for i, num in enumerate(alst):
    ans -= num * nCk(n - 1 - i, k - 1)
    ans %= MOD

for i, num in enumerate(alst[::-1]):
    ans += num * nCk(n - 1 - i, k - 1)
    ans %= MOD
print(ans)
