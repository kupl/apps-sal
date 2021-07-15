MOD = 10**9+7

N = int(input())

cnt = (pow(10, N, MOD) - 2*pow(9, N, MOD) + pow(8, N, MOD))
cnt = cnt % MOD

print(cnt)
