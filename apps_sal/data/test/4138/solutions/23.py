from functools import *


def sumnum(start, end):
    return end * (end - 1) // 2 - start * (start - 1) // 2


def digits(i):
    return len(f'{i}')


@lru_cache(maxsize=32)
def digit_count(i):
    if i == 0:
        return 0
    d = digits(i)
    base = 10 ** (d - 1) - 1
    return digit_count(base) + d * (i - base)


@lru_cache(maxsize=32)
def cumulative_digit_count(i):
    if i == 0:
        return 0
    d = digits(i)
    base = 10 ** (d - 1) - 1
    return cumulative_digit_count(base) + digit_count(base) * (i - base) + d * sumnum(base + 1, i + 1) - d * base * (i - base)


def bin_search(k, f):
    for d in range(1, 20):
        if f(10 ** (d - 1) - 1) > k:
            break
    upper = 10 ** (d - 1) - 1
    lower = 10 ** (d - 2) - 1
    while upper - lower > 1:
        middle = (lower + upper) // 2
        if f(middle) > k:
            upper = middle
        else:
            lower = middle
    return (lower, k - f(lower))


def answer(q):
    (lower1, k) = bin_search(q, cumulative_digit_count)
    if k == 0:
        return lower1 % 10
    (lower2, l) = bin_search(k, digit_count)
    if l == 0:
        return lower2 % 10
    return int(f'{lower2 + 1}'[l - 1])


def naive_cum(i):
    cum = 0
    for ii in range(1, i + 1):
        for j in range(1, ii + 1):
            cum = cum + len(f'{j}')
    return cum


a = input()
for i in range(int(a)):
    q = input()
    print(answer(int(q)))
