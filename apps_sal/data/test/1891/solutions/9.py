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


(n, k, A, B) = mi()
avg = lm()


def divide(startbin, endbin, level, currentas, currentlength):
    if currentlength == 0:
        return A
    astart = []
    aend = []
    midpoint = startbin * 2 ** (n - level)
    for a in currentas:
        if a <= midpoint:
            astart.append(a)
        else:
            aend.append(a)
    binlength = 2 ** (n - level)
    a1 = len(astart)
    a2 = len(aend)
    cost1 = (a1 + a2) * B * (binlength * 2)
    if level == n:
        if a1 == 0:
            subcost1 = A
        else:
            subcost1 = B * a1
        if a2 == 0:
            subcost2 = A
        else:
            subcost2 = B * a2
        cost2 = subcost1 + subcost2
    else:
        cost2 = divide(startbin * 2 - 1, startbin * 2, level + 1, astart, a1) + divide(endbin * 2 - 1, endbin * 2, level + 1, aend, a2)
    return min(cost1, cost2)


print(divide(1, 2, 1, avg, k))
