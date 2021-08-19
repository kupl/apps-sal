import bisect
import heapq
import itertools
import sys
import math
import random
import time
from collections import Counter, deque, defaultdict
from functools import reduce
from operator import xor
from types import FunctionType
from typing import List, Any
from sys import stdin

mod = 10 ** 9 + 7
sys.setrecursionlimit(10 ** 9)


def lmi():
    return list(map(int, stdin.readline().split()))


def narray(*shape, init: Any = 0):
    if shape:
        num = shape[0]
        return [narray(*shape[1:], init=init) for _ in range(num)]
    if callable(init):
        return init()
    return init


def main():
    N = int(input())
    AA = input()
    AB = input()
    BA = input()
    BB = input()
    ans = solve(N, AA, AB, BA, BB)
    print(ans)
    # for i in range(2, 10):
    #     for pattern in itertools.product('AB', repeat=4):
    #         N = i
    #         ans = stupid(N, *pattern)
    #         print(ans, *pattern)
    #         # assert ans == solve(N, *pattern)
    #     print('-' * 100)

    # if AB == 'A':
    #     if AA == 'A':
    #         print(1)
    #         return
    #     else:
    #         # AB: A, AA: B
    #         pass
    # else:
    #     if BB == 'B':
    #         print(1)
    #     else:
    #         pass


def solve(N, AA, AB, BA, BB):
    pattern = ''.join([AA, AB, BA, BB])
    ans = 1
    if pattern in [
        'AAAA',
        'AAAB',
        'AABA',
        'AABB',
        'ABAB',
        'ABBB',
        'BBAB',
        'BBBB',
    ]:
        ans = f1(N)
    elif pattern in [
        'ABAA',
        'BABA',
        'BABB',
        'BBAA',
    ]:
        ans = f2(N)
    elif pattern in [
        'ABBA',
        'BAAA',
        'BAAB',
        'BBBA',
    ]:
        ans = f3(N - 1)
    return ans


def f1(N):
    return 1


def f2(N):
    return pow(2, max(0, N - 3), mod)


def f3(N):
    memo = [0] * (N + 3)
    memo[1] = 1
    memo[2] = 1
    for i in range(3, N + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
        memo[i] %= mod
    return memo[N]


def stupid(N, AA, AB, BA, BB):
    ret = set()
    stack = ['AB']
    while stack:
        cur = stack.pop()
        if len(cur) == N:
            ret.add(cur)
            continue
        for i in range(len(cur) - 1):
            next_s = ''
            if cur[i: i + 2] == 'AA':
                next_s = cur[:i + 1] + AA + cur[i + 1:]
            elif cur[i: i + 2] == 'AB':
                next_s = cur[:i + 1] + AB + cur[i + 1:]
            elif cur[i: i + 2] == 'BA':
                next_s = cur[:i + 1] + BA + cur[i + 1:]
            elif cur[i: i + 2] == 'BB':
                next_s = cur[:i + 1] + BB + cur[i + 1:]
            stack.append(next_s)
    # print(ret)
    return len(ret)


def __starting_point():
    main()


__starting_point()
