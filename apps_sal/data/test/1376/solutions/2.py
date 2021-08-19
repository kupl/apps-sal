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
d = {}
for i in range(2 * n):
    if l[i] in d:
        d[l[i]].append(i)
    else:
        d[l[i]] = [i]
s1 = 0
s2 = 0
tot = 0
for i in range(n):
    d1 = d[i + 1][0]
    d2 = d[i + 1][1]
    dist = min(abs(s1 - d1) + abs(s2 - d2), abs(s1 - d2) + abs(s2 - d1))
    tot = tot + dist
    s1 = d1
    s2 = d2
print(tot)
