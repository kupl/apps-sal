n, m = map(int, input().split())
MOD = 1000000007
res = pow(2, m, MOD) - 1
res = pow(res, n, MOD)
print(res)
