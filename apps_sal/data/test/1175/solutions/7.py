import os
import os
import sys
from collections import defaultdict

import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7

L, R = list(map(int, sys.stdin.readline().split()))


def test(L, R):
    ans = 0
    cnt = defaultdict(int)
    for x in range(L, R + 1):
        for y in range(x, R + 1):
            if y % x == y ^ x:
                cnt[x + y % x] += 1
                ans += 1
    return ans


def solve(L, R):
    ret = L == 1
    for msb in range(R.bit_length()):
        r = min(R, (1 << msb + 1) - 1)
        l = max(L, (1 << msb))
        if l > r:
            continue
        # print(bin(r), bin(l))
        # dp[d][n][rより下を選んだ][lより上を選んだ]
        dp = np.zeros((r.bit_length(), 2, 2), dtype=int)
        for d in reversed(list(range(r.bit_length() - 1))):
            dp[-1][0][0] = 1
            if r >> d & 1:
                if l >> d & 1:
                    # r == 1, l == 1
                    # y1, x1
                    dp[d][1][1] += dp[d + 1][1][1]
                    dp[d][1][0] += dp[d + 1][1][0]
                    dp[d][0][1] += dp[d + 1][0][1]
                    dp[d][0][0] += dp[d + 1][0][0]
                    # y1, x0
                    dp[d][1][1] += dp[d + 1][1][1]
                    dp[d][0][1] += dp[d + 1][0][1]
                    # y0, x0
                    dp[d][1][1] += dp[d + 1][1][1]
                    dp[d][1][1] += dp[d + 1][0][1]
                else:
                    # r == 1, l == 0
                    # y1, x1
                    dp[d][1][1] += dp[d + 1][1][1]
                    dp[d][1][1] += dp[d + 1][1][0]
                    dp[d][0][1] += dp[d + 1][0][1]
                    dp[d][0][1] += dp[d + 1][0][0]
                    # y1, x0
                    dp[d][1][1] += dp[d + 1][1][1]
                    dp[d][1][0] += dp[d + 1][1][0]
                    dp[d][0][1] += dp[d + 1][0][1]
                    dp[d][0][0] += dp[d + 1][0][0]
                    # y0, x0
                    dp[d][1][1] += dp[d + 1][1][1]
                    dp[d][1][0] += dp[d + 1][1][0]
                    dp[d][1][1] += dp[d + 1][0][1]
                    dp[d][1][0] += dp[d + 1][0][0]
            else:
                if l >> d & 1:
                    # r == 0, l == 1
                    # y1, x1
                    dp[d][1][1] += dp[d + 1][1][1]
                    dp[d][1][0] += dp[d + 1][1][0]
                    # y1, x0
                    dp[d][1][1] += dp[d + 1][1][1]
                    # y0, x0
                    dp[d][1][1] += dp[d + 1][1][1]
                    dp[d][0][1] += dp[d + 1][0][1]
                else:
                    # r == 0, l == 0
                    # y1, x1
                    dp[d][1][1] += dp[d + 1][1][1]
                    dp[d][1][1] += dp[d + 1][1][0]
                    # y1, x0
                    dp[d][1][1] += dp[d + 1][1][1]
                    dp[d][1][0] += dp[d + 1][1][0]
                    # y0, x0
                    dp[d][1][1] += dp[d + 1][1][1]
                    dp[d][1][0] += dp[d + 1][1][0]
                    dp[d][0][1] += dp[d + 1][0][1]
                    dp[d][0][0] += dp[d + 1][0][0]
            dp[d] %= MOD
        ret += dp[0].sum()
        ret %= MOD
    return int(ret)


print((solve(L, R)))
# for l in range(1, R + 1):
#     for r in range(l, R + 1):
#         t1, t2 = solve(l, r), test(l, r)
#         if t1 != t2:
#             print(bin(l), bin(r), l, r, t1, t2)
