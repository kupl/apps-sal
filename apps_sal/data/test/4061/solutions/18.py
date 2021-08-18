import sys
from collections import defaultdict
import math


def main():
    s = input()
    t = input()
    longest_prefix = [0] * len(s)
    longest_suffix = [0] * len(s)

    longest_prefix[0] = 1 if s[0] == t[0] else 0
    for i in range(1, len(s)):
        x = longest_prefix[i - 1]
        if x == len(t) or s[i] != t[x]:
            longest_prefix[i] = x
        else:
            longest_prefix[i] = x + 1

    longest_suffix[-1] = 1 if s[-1] == t[-1] else 0
    for i in range(len(s) - 2, -1, -1):
        x = longest_suffix[i + 1]
        if x == len(t) or s[i] != t[-1 - x]:
            longest_suffix[i] = x
        else:
            longest_suffix[i] = x + 1

    res = 0

    pos1 = 0
    while longest_prefix[pos1] != len(t):
        pos1 += 1
    res = max(res, len(s) - 1 - pos1)

    pos2 = len(s) - 1
    while longest_suffix[pos2] != len(t):
        pos2 -= 1
    res = max(res, pos2)

    pos1 = 0
    pos2 = 0
    while pos1 < len(s):
        while pos2 + 1 < len(s) and longest_prefix[pos1] + longest_suffix[pos2 + 1] >= len(t):
            pos2 += 1
        res = max(res, pos2 - pos1 - 1)
        pos1 += 1

    print(res)


def __starting_point():
    main()


__starting_point()
