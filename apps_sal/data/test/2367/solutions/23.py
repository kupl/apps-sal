import math
import heapq
import bisect
import numpy as np
from collections import Counter, deque
import itertools
MOD = 10 ** 9 + 7
(H, W, A, B) = map(int, input().split())


def comb(a, b):
    p = fac[a - b] * fac[b] % MOD
    return fac[a] * pow(p, MOD - 2, MOD) % MOD


fac = [1]
for i in range(H + W):
    fac.append(fac[-1] * (i + 1) % MOD)
ans = 0
for i in range(W - B):
    p = comb(H - A - 1 + B + i, B + i) * comb(W - B - i - 2 + A, A - 1)
    ans += p % MOD
    ans %= MOD
print(ans)
