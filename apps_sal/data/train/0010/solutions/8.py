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


q = nn()

for _ in range(q):
    n = nn()

    per = lm()

    best = [per[0]]

    for i in range(len(per) - 2):
        minper = min(per[i], per[i + 1], per[i + 2])
        maxper = max(per[i], per[i + 1], per[i + 2])
        if minper == per[i + 1] or maxper == per[i + 1]:
            best.append(per[i + 1])
    best.append(per[-1])
    print(len(best))
    print(*best)
