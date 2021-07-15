import sys
import re
import math
import collections
import decimal
import bisect
import itertools
import fractions
import functools
import copy
import heapq
import decimal
import statistics
import queue

# import numpy as np

sys.setrecursionlimit(10 ** 9)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: list(map(int, sys.stdin.readline().split()))
na = lambda: list(map(int, sys.stdin.readline().split()))
nb = lambda: list([int(x) - 1 for x in sys.stdin.readline().split()])


# ===CODE===


def main():
    n = ni()
    match = [collections.deque(nb()) for _ in range(n)]

    nxt = [-1] * n
    waiting = collections.deque(list(range(n)))
    cnt = [0] * n

    while len(waiting) > 0:
        ego = waiting.popleft()
        if len(match[ego]) == 0:
            continue

        enemy = match[ego].popleft()

        if nxt[enemy] == ego:
            waiting.append(ego)
            waiting.append(enemy)
            cnt[ego] = cnt[enemy] = max(cnt[ego], cnt[enemy]) + 1

        else:
            nxt[ego] = enemy

    if any(match):
        print((-1))
    else:
        print((max(cnt)))


def __starting_point():
    main()

__starting_point()
