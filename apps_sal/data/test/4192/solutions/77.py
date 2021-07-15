# -*- coding utf-8 -*-

MOD = 10 ** 9 + 7

D, T, S = list(map(int, input().split()))

ans = 'Yes' if S * T >= D else 'No'

print(ans)

