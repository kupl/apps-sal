import sys
from math import factorial

MOD = 998244353

INF = float('inf')

A, B, C = list(map(int, input().split()))

aa = (A * (A + 1) // 2) % MOD
bb = (B * (B + 1) // 2) % MOD
cc = (C * (C + 1) // 2) % MOD

out = (aa * bb * cc) % MOD

print(("{}".format(out)))
