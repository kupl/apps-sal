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


n = li()

digits = [int(i) for i in n]

ma = 0
prod = 1
for j in digits:
    prod = prod * j

ma = max(ma, prod)


for i in range(1, len(digits)):
    if not digits[~i] == 0:
        digits[~i] -= 1
        j = 1

        while i - j >= 0:
            digits[~(i - j)] = 9
            j += 1
    else:
        continue

    prod = 1
    for j in range(len(digits)):
        if not (j == 0 and digits[j] == 0):
            prod = prod * digits[j]

    ma = max(ma, prod)


print(ma)
