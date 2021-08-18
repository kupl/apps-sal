n = int(input())

MOD = 10 ** 9 + 7

print((pow(10, n) % MOD - (9**n * 2 - 8 ** n) % MOD) % MOD)
