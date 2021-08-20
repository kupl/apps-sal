N = int(input())
MOD = 10 ** 9 + 7
All = 10 ** N % MOD
nine_all = 9 ** N % MOD
eight_all = 8 ** N % MOD
ans = All - (2 * nine_all - eight_all)
ans %= MOD
print(ans)
