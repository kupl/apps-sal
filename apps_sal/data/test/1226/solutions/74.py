"""
Created on Sun Sep 13 19:51:37 2020

@author: liang
"""

import math

key = 10**9 + 7

n, a, b = map(int, input().split())

ans = 1
tmp = 2
N = math.ceil(math.log2(n))

for i in range(N + 1):
    if n >> i & 1 == 1:
        ans *= tmp
    tmp *= tmp
    tmp %= key
    ans %= key
ans -= 1


def comb(r):
    perm = 1
    for i in range(0, r):
        perm *= n - i
        perm %= key

    fact = 1
    for i in range(1, r + 1):
        fact *= i
        fact %= key

    ans = 1
    tmp = fact
    p = key - 2
    N = math.ceil(math.log2(p))
    for i in range(N):
        if p >> i & 1 == 1:
            ans *= tmp
        tmp *= tmp
        tmp %= key
        ans %= key
    ans *= perm
    ans %= key
    return ans


ans -= comb(a)
ans -= comb(b)
ans %= key
print(ans)
