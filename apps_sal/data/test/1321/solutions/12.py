#!/usr/bin/env python3
from sys import stdin

n = int(stdin.readline().strip())
w, h = list(), list()
w_sum = 0
h_max = 0
h_second = 0
for i in range(n):
    cur_w, cur_h = map(int, stdin.readline().strip().split())
    w.append(cur_w)
    w_sum += cur_w
    if cur_h <= h_max and cur_h > h_second:
        h_second = cur_h
    if cur_h > h_max:
        h_second = h_max
        h_max = cur_h
        h_max_index = i
        has_single_max = True
    elif cur_h == h_max:
        has_single_max = False

for i in range(n):
    print((w_sum - w[i]) * (h_max if not has_single_max or i != h_max_index else h_second), end=' ')

