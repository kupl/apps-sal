#!/usr/bin python3
# -*- coding: utf-8 -*-

import itertools
L = [''.join(i) for i in itertools.product('0123', repeat=3)]
l = len(L)

mod = 10**9+7

AGC = '021'
ACG = '012'
GAC = '201'
nc3 = set([AGC, ACG, GAC])

AGGC = '0221'
AGTC = '0231'
ATGC = '0321'
nc4 = set([AGGC, AGTC, ATGC])

n = int(input())
dp = [[0]*l for _ in range(n+1)]
for i in L:
    if i in nc3: continue
    dp[3][int(i, 4)] = 1

for i in range(3, n):
    for jl in L:
        for k in "0123":
            nxt = jl[1:] + k
            if nxt in nc3: continue
            if jl+k in nc4: continue
            dp[i+1][int(nxt, 4)] += dp[i][int(jl, 4)]
print((sum(dp[n])%mod))

