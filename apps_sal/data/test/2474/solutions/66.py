N = int(input())
C = list(map(int, input().split()))
C = reversed(sorted(C))

MOD = 10 ** 9 + 7
pow = 4 ** (N - 1) % MOD

ans = 0
for i, c in zip(range(N), C):
    ans += (i + 2) * c % MOD
    ans %= MOD

print(ans * pow % MOD)
