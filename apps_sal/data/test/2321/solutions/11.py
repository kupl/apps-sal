from collections import defaultdict as dd
import math


def nn():
    return int(input())


def li():
    return list(input())


def mi():
    return list(map(int, input().split()))


def lm():
    return list(map(int, input().split()))


n = nn()

for i in range(n):
    l = nn()

    s = li()

    leftmin = 0
    rightmin = 0

    while leftmin < len(s) and s[leftmin] == '<':
        leftmin += 1

    while rightmin < len(s) and s[~rightmin] == '>':
        rightmin += 1

    print(min(leftmin, rightmin))
