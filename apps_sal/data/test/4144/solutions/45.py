MOD = 10**9 + 7

N = int(input())

a1 = pow(10, N, MOD)
a2 = 2 * pow(9, N, MOD)
a3 = pow(8, N, MOD)
ans = (a1 - a2 + a3) % MOD

print(ans)
