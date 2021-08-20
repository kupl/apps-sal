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
    cakes = lm()
    cake_count = [0] * (n + 10)
    for cake in cakes:
        cake_count[cake] += 1
    most = max(cake_count)
    k = 0
    for num in cake_count:
        if num == most:
            k += 1
    print((n - most * k) // (most - 1) + (k - 1))


q = nn()
for _ in range(q):
    solve()
