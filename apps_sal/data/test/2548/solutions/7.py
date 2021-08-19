from collections import defaultdict as dd
import math
import sys
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
    n = nn()
    l = input()
    seen = dd(int)
    seen[0] = 1
    tally = 0
    good = 0
    for i in range(n):
        tally += int(l[i]) - 1
        seen[tally] += 1
    total = 0
    for s in seen:
        total += seen[s] * (seen[s] - 1) // 2
    print(total)


q = nn()
for _ in range(q):
    solve()
