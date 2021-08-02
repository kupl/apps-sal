#!/usr/bin/env python3
import itertools
import numpy as np

H, W, K = list(map(int, input().split()))
c_table = []

for _ in range(H):
    c_list = input()
    c_list = [0 if c == "." else 1 for c in list(c_list)]
    c_table.append(c_list)

h_patterns = list(itertools.product([True, False], repeat=H))
w_patterns = list(itertools.product([True, False], repeat=W))
count = 0
for h_p in h_patterns:
    for w_p in w_patterns:
        w_table = np.array(c_table)

        for i, h_flag in enumerate(h_p):
            if h_flag:
                w_table[i] = 0
            for j, w_flag in enumerate(w_p):
                if w_flag:
                    w_table.T[j] = 0
        if w_table.sum() == K:
            count += 1

ans = count

print(ans)
