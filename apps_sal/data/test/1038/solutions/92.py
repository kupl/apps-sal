# 偶数a ^ (a + 1)　は必ず1になる
# 従い、0 〜 4の倍数 - 1でXORは0になる

import sys
readline = sys.stdin.readline

A, B = list(map(int, readline().split()))


def f(x):
    res = 0
    while x % 4 != 3:
        res ^= x
        x -= 1
    return res


print((f(A - 1) ^ f(B)))
