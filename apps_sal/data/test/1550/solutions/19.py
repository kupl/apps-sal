#!/usr/bin/env python3

n = int(input())
state = [int(c) for c in input()]
min_s = state
for i in range(n):
    tmp = state[i:] + state[:i]
    tmp_min = [tmp[i] - tmp[0] for i in range(n)]
    for i in range(n):
        if tmp_min[i] < 0:
            tmp_min[i] += 10
    if tmp_min < min_s:
        min_s = tmp_min
print("".join(map(str, min_s)))
