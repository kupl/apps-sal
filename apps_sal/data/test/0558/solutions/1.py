from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque,Counter
from operator import mul
import copy
# ! /usr/bin/env python
# -*- coding: utf-8 -*-

import heapq

m = 2*10**5
mod = 998244353

fact = [0]*(m+5)
fact_inv = [0]*(m+5)
inv = [0]*(m+5)

fact[0] = fact[1] = 1
fact_inv[0] = fact_inv[1] = 1
inv[1] = 1

for i in range(2,m+5):
    fact[i] = fact[i-1] * i % mod
    inv[i] = mod - inv[mod % i] * (mod // i) % mod
    fact_inv[i] = fact_inv[i-1] * inv[i] % mod

# nCkをmod（素数）で割った余りを求める．ただしn<10**7
# 前処理はm=n+5まで
def cmb(n,k,mod):
    return fact[n] * (fact_inv[k] * fact_inv[n-k] % mod) % mod

ans = 0

n,m,k = list(map(int, input().split()))
for i in range(k+1):
    ans = (ans + (m*cmb(n-1,i,mod) % mod)*(pow(m-1,n-1-i,mod)) % mod) % mod

print(ans)
