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


n, m = mi()


lowend = max(1, m)

highend = n - m

print(min(lowend, highend))
