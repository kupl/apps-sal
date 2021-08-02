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


n, v = mi()

dist = n - 1

if v >= dist:
    print(dist)

else:
    off = dist - v
    prices = [i + 2 for i in range(off)]
    print(v + sum(prices))
