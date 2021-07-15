import os
import os
import sys
from functools import reduce
from operator import xor

import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A = np.array(A, dtype=np.int64)


def dump(arr):
    for a in arr:
        print((np.binary_repr(a, 60)))
    print()


# 解説AC
# 立ってるビットが奇数ならどう分けても結果は同じ
odds = reduce(xor, A)
ans = odds

# 奇数のやつは無視
A &= ~odds

# 行標準形にする
# https://qiita.com/vain0x/items/015ff6d49853e5d9d403#f---xor-sum-3
rank = 0
for d in reversed(list(range(60))):
    # 下からd桁目が立ってる最初のindex
    bits1 = (A >> d & 1).astype(bool)
    pos = bits1[rank:].argmax() + rank
    if not bits1[pos]:
        continue  # 全部ゼロ
    if pos < rank:
        continue  # rank より下に 1 がない。どう頑張っても変えられない。(?)

    # 基準にする行
    pivot_row = A[pos]
    # 基準以外を全部ゼロにする
    A[bits1] ^= pivot_row
    A[pos] = pivot_row
    # 基準行を一番上に持ってくる
    A[pos], A[rank] = A[rank], A[pos]
    rank += 1

ans += reduce(xor, A) * 2
print(ans)

