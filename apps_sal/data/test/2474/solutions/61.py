MOD = 10**9 + 7
n = int(input())
S = [1] * n
D = [1] * (n + 1)
for i in range(n):
    D[i + 1] = D[i] * 2 % MOD
for i in range(n - 1):
    S[i + 1] = (S[i] * 2 + D[i + 1]) % MOD
T = S[::-1]
C = sorted(list(map(int, input().split())))
ans = 0
for i in range(n):
    ans += C[i] * ((D[n - (i + 1)] + T[i]) * D[i]) % MOD
    ans %= MOD
ans = ans * D[n - 1] % MOD
print(ans)
