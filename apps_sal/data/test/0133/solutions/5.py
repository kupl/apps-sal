n, m = list(map(int, input().split()))
MOD = 10**9 + 7
print(pow(pow(2, m, MOD) - 1, n, MOD))

