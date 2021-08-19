import math
import re
from pprint import pprint as pprint
from collections import Counter
import itertools as ittls
3


def sqr(x):
    return x * x


def inputarray(func=int):
    return list(map(func, input().split()))

# --------------------------------------
# --------------------------------------


N = int(input())
A = list(inputarray())

power, i = 0, 0
mask = [0] * N

while power < N:
    s = 0

    domain = list(range(N)) if i & 1 != 1\
        else list(range(N - 1, -1, -1))
    for j in domain:
        if mask[j] == 0 and A[j] <= power:
            mask[j] = 1
            power = power + 1

    i = i + 1

print(i - 1)
