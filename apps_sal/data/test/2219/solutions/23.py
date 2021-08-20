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


q = nn()
for _ in range(q):
    (n, k) = mi()
    moves = 0
    while n >= k:
        moves += n % k + 1
        n = n // k
    moves += n
    print(moves)
