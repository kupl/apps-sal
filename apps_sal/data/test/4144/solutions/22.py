# -*- coding utf-8 -*-

MOD = 10 ** 9 + 7

N = int(input())

ans = pow(10, N, MOD) - (pow(9, N, MOD) * 2 - pow(8, N, MOD))

ans %= MOD
print(ans)

