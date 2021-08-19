#!/usr/bin/env python3
import itertools
import math

d, g = list(map(int, input().split()))
pc = [list(map(int, input().split())) for i in range(d)]


ans = 100 * d * 100
for d in itertools.product([0, 1], repeat=d):
    ans_tmp = 0
    value = 0

    for i, j in enumerate(d):
        if j == 0:
            continue
        ans_tmp += pc[i][0]
        value += (i + 1) * 100 * pc[i][0] + pc[i][1]

    iter_ = [[i, j] for i, j in enumerate(d)]
    # print(iter_)
    for i, j in reversed(iter_):
        if j == 1:
            continue
        base = (i + 1) * 100

        shortage = g - value
        if g - value <= 0:
            break

        num = min(math.ceil(shortage / base), pc[i][0] - 1)
        ans_tmp += num
        value += base * num
    # print(d)
    # print(value, ans_tmp)
    if value >= g:
        ans = min(ans, ans_tmp)

print(ans)
