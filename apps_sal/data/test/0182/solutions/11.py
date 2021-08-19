__author__ = 'MoonBall'

import sys
# sys.stdin = open('data/A.in', 'r')
T = 1


def process():
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    delta = 0
    sum_delta = 0
    for _a, _b in zip(a, b):
        if _a < _b:
            delta += _b - _a
        else:
            sum_delta += (_a - _b) // 2

    print('Yes' if sum_delta >= delta else 'No')


for _ in range(T):
    process()
