# -*- coding: utf-8 -*-
import sys

N, M, K = list(map(int, input().rstrip().split()))
# -----

if (M == 1) and (K == N - 1):
    print((1))
    return
elif (M == 1) and (K < N - 1):
    print((0))
    return


mod = 998244353

a = M * pow(M - 1, N - 1, mod)
inv_M1 = pow((M - 1), mod - 2, mod)  # inverse element

comb = 1
ans = 0

for i in range(K + 1):
    ans += (comb * a)
    ans %= mod

    # Calculate variables for next step
    a *= inv_M1
    a %= mod

    inv_i1 = pow(i + 1, mod - 2, mod)  # inverse element
    comb *= ((N - 1 - i) * inv_i1)
    comb %= mod


print(ans)
