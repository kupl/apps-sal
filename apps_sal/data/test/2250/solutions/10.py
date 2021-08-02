from collections import defaultdict as dd
import math
import sys
import heapq
import copy
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

    s = input()

    streaks = []
    st = 1
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            st += 1
        else:
            streaks.append(st)
            st = 1

    #print(st, s[0], s[n-1])
    if s[0] == s[n - 1] and len(streaks) > 0:
        streaks[0] += st
    else:
        streaks.append(st)
    # print(streaks)
    moves = 0
    # print(streaks)
    if len(streaks) == 1:
        moves = (streaks[0] - 1) // 3 + 1
    else:
        for num in streaks:
            moves += num // 3

    print(moves)


q = nn()

for _ in range(q):
    solve()
