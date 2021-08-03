# author:  Taichicchi
# created: 20.09.2020 11:13:28

import sys

from math import factorial

from scipy.special import comb

MOD = 10 ** 9 + 7

S = int(input())

m = S // 3

cnt = 0

for n in range(1, m + 1):
    cnt += int(comb(S - 3 * n + 1, n - 1, exact=True, repetition=True)) % MOD

cnt %= MOD

print(cnt)
