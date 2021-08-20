N = int(input())
C = sorted(list(map(int, input().split())))[::-1]
ans = 0
MOD = 10 ** 9 + 7
for k in range(N):
    ans += pow(2, 2 * N - 2, MOD) * (k + 2) * C[k]
print(ans % MOD)
