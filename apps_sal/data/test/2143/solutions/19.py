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
for i in range(n):
    for j in range(i + 1, n):
        s = l[i] + l[j]
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
m = 0
for s in d:
    m = max(m, d[s])
print(m)
