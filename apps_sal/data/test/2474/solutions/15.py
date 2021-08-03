N = int(input())
MOD = 10**9 + 7
C = list(map(int, input().split()))
C.sort()

ans = 0
for i, c in enumerate(C, start=1):
    M = N - i
    ans += c * (M + 2)
    ans %= MOD
ans *= pow(4, N - 1, MOD)
print((ans % MOD))
