"""input
3 2 1
6 3 2
5 3 0
3 3 1
3 3 0
"""
(n, m, k) = list(map(int, input().split()))
MOD = 998244353
ans = m * pow(m - 1, k, MOD) % MOD
'\nfor i in range(k + 1):\n\tif i & 1:\n\t\tans -= m * pow(m - 1, k - i, MOD)\n\telse:\n\t\tans += m * pow(m - 1, k - i, MOD)\n'
for i in range(n - k, n):
    ans = ans * i
for i in range(n - k, n):
    ans = ans // (n - i)
'\nfor i in range(1, k + 1):\n\tprint(ans)\n\tans = ans * (n - 1 - i) * pow(i, MOD - 2, MOD) % MOD\n'
print(ans % MOD)
