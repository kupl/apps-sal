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
    s = input()
    sets = []
    streak = 0
    for i in range(len(s)):
        if s[i] == '1':
            streak += 1
        elif streak > 0:
            sets.append(streak)
            streak = 0
    if streak > 0:
        sets.append(streak)
        streak = 0
    sets.sort(reverse=True)
    print(sum(sets[::2]))


q = nn()
for _ in range(q):
    solve()
