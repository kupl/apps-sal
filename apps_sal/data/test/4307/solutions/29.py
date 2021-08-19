import math
from collections import Counter
from itertools import product


def ii():
    return int(input())


def mi():
    return list(map(int, input().split()))


def li():
    return list(map(int, input().split()))


def make_divisors(n):
    (lower_div, upper_div) = ([], [])
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_div.append(i)
            if i != n // i:
                upper_div.append(n // i)
        i += 1
    return lower_div + upper_div[::-1]


n = ii()
cnt = 0
for i in range(1, n + 1, 2):
    if len(make_divisors(i)) == 8:
        cnt += 1
print(cnt)
