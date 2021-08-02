import sys
import math
from functools import lru_cache
from collections import deque
from bisect import bisect_left
sys.setrecursionlimit(10**9)


def input():
    return sys.stdin.readline()[:-1]


def mi():
    return list(map(int, input().split()))


def ii():
    return int(input())


def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]


def main():
    N, M = mi()

    d = []
    i = 1
    while i * i <= M:
        if M % i == 0:
            d.append(i)
            d.append(M // i)
        i += 1

    d.sort()

    for v in d:
        if v <= M // N:
            ans = v
        else:
            break

    print(ans)


def __starting_point():
    main()


__starting_point()
