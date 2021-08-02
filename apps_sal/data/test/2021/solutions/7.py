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

l = lm()

q = nn()

qs = lm()

l.sort()

s = sum(l)

for c in qs:
    print(s - l[-c])
