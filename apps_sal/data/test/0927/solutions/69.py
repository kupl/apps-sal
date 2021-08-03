import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
def input(): return sys.stdin.readline().strip()
def NI(): return int(input())
def NMI(): return map(int, input().split())
def NLI(): return list(NMI())
def SI(): return input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N, M = NMI()
    A = NLI()

    match_dict = {i + 1: m for i, m in enumerate([2, 5, 5, 4, 5, 6, 3, 7, 6])}
    usable_list = [[a, match_dict[a]] for a in A]
    usable_list.sort(key=lambda x: (x[1], -x[0]))

    # dp[i] はi本使った時の最大数
    dp = [-1] * (N + 10)
    dp[0] = 0

    for i in range(N + 1):
        for num, m in usable_list:
            dp[i + m] = max(dp[i + m], dp[i] * 10 + num)
    print(dp[N])


def __starting_point():
    main()


__starting_point()
