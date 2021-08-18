# ----------------
# ここから
# ----------------

import sys
from io import StringIO
import unittest


def resolve():
    readline = sys.stdin.readline
    mod = 10**9 + 7
    n = int(readline())
    arr = list(map(int, readline().rstrip().split()))
    ans = 0
    x = 1
    for i in range(60):
        c = 0
        for j in range(n):
            if arr[j] & x != 0:
                c += 1
        ans += (c * (n - c)) * x
        ans %= mod
        x = x * 2
    print(ans)
    return


if 'doTest' not in globals():
    resolve()
    return

# ----------------
# ここまで
# ----------------
