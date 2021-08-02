def power(n, r, mod=10**9 + 7):
    if r == 0: return 1
    if r % 2 == 0:
        return power(n * n % mod, r // 2, mod) % mod
    if r % 2 == 1:
        return n * power(n, r - 1, mod) % mod


N = int(input())
C = list(map(int, input().split()))
C.sort()
MOD = 10**9 + 7

ans = 0
for i, c in enumerate(C, 1):
    ans = (ans + (N - i + 2) * c) % MOD

ans *= power(4, N - 1)
ans %= MOD
print(ans)
