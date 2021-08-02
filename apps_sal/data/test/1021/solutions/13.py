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

Gs = lm()

As = lm()

diffsG = [Gs[i] - Gs[i - 1] for i in range(1, n)]

diffsA = [As[i] - As[i - 1] for i in range(1, n)]


diffsG.sort()

diffsA.sort()

if Gs[0] == As[0] and diffsG == diffsA:
    print('Yes')
else:
    print('No')
