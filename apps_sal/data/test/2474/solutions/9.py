N = int(input())
C = [0] + sorted(list(map(int, input().split())))
MOD = 10 ** 9 + 7
ans = 0
for i in range(1, N + 1):
    (l, r) = (i - 1, N - i)
    ans += C[i] * pow(2, l, MOD) * (pow(2, max(0, r - 1), MOD) * r % MOD + pow(2, r, MOD)) % MOD
print(ans * pow(2, N, MOD) % MOD)
