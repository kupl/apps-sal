from collections import defaultdict as dd
import math
import sys
import string
input = sys.stdin.readline


def nn():
    return int(input())


def li():
    return list(input())


def mi():
    return list(map(int, input().split()))


def lm():
    return list(map(int, input().split()))


def solve():
    (r, g, b, w) = mi()
    par = r % 2 + g % 2 + b % 2 + w % 2
    if par <= 1:
        print('Yes')
        return
    elif r >= 1 and g >= 1 and (b >= 1):
        if par == 3 or par == 4:
            print('Yes')
            return
    print('No')


q = nn()
for _ in range(q):
    solve()
