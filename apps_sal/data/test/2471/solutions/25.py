"""
参考(神様)
https://atcoder.jp/contests/abc045/submissions/6046010
"""

# かぶるやつを考える.例えばあるマスのかぶり値が9だとしたら,
# 周囲はすべて黒->j=9のが1つとカウントしてよい,他の値についても同様.

import sys
from collections import defaultdict, Counter


def input():
    return sys.stdin.readline().strip()


H, W, N = map(int, input().split())

covered = defaultdict(int)
vector = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

for _ in range(N):
    a, b = map(int, input().split())

    for i, j in vector:
        x = a + i - 1
        y = b + j - 1

        if 0 < x < H - 1 and 0 < y < W - 1:
            covered[(x, y)] += 1

num = Counter(covered.values())
# print(num)
num[0] = (H - 2) * (W - 2) - sum(num.values())

for i in range(10):
    print(num[i])
