import sys
import re
from collections import deque, defaultdict
from itertools import combinations, combinations_with_replacement
import bisect
from math import factorial, sqrt, log, ceil, floor
sys.setrecursionlimit(1000000)


def solve(S, N, K, LR):
    happy = 0
    one = 0
    two = 0
    prev = None
    for i in range(N + 1):
        s = S[i]
        if prev is None:
            prev = (s, i)
            continue
        if prev[0] == s:
            continue
        happy += i - 1 - prev[1]
        if prev[0] == LR:
            if prev[1] == 0 and i - 1 == N - 1:
                pass
            elif prev[1] == 0 or i - 1 == N - 1:
                one += 1
            else:
                two += 1
        prev = (s, i)
    spans = [2] * two + [1] * one
    if spans:
        happy += sum(spans[:min(K, len(spans))])
    return happy


def main():
    input = sys.stdin.readline
    (N, K) = list(map(int, input().split()))
    S = input().strip()
    S += 'D'
    happy = max([solve(S, N, K, 'L'), solve(S, N, K, 'R')])
    print(happy)


def __starting_point():
    main()


__starting_point()
