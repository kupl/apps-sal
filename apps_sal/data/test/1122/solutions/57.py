import os
from collections import Counter

import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7


N, M = list(map(int, sys.stdin.buffer.readline().split()))


def test(ans):
    hist = []
    for a, b in ans:
        hist.append((0, (b - a) % N))
        hist.append((0, (a - b) % N))
    print((len(set(hist)) == M * 2))
    print((Counter(hist)))


ans = []
if N % 2 == 1:
    for i in range(M):
        a, b = i + 1, N - i
        ans.append((a, b))
else:
    hist = set()
    d = 0
    for i in range(M):
        a, b = i + 1, N - i - d
        if (a - b) % N in hist or (b - a) % N in hist or (a - b) % N == (b - a) % N:
            d += 1
            a, b = i + 1, N - i - d
        hist.add((a - b) % N)
        hist.add((b - a) % N)
        ans.append((a, b))

for a, b in ans:
    print((a, b))
