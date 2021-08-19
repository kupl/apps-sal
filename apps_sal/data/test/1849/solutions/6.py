# from io import BytesIO
# import os
# input = BytesIO(os.read(0, os.fstat(0).st_size)).readline

n = int(input())
MOD = 998244353
for k in range(1, n):
    t = ((n - k - 1) * 81 * pow(10, n - k - 2, MOD) * 10 + 10 * 9 * pow(10, n - k - 1, MOD) * 2) % MOD
    print(t, end=' ')
print(10)
