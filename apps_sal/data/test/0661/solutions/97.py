# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# # 問題：https://atcoder.jp/contests/abc126/tasks/abc126_f
# # 解説動画を見ながら実装

import sys

m, k = map(int, input().strip().split())
max_num = 2**m
if k >= max_num:
    print(-1)
    return

# if m == 0:
#     print(0)
#     return

if m == 1:
    if k == 0:
        print('0 0 1 1')
    else:
        print('-1')
    return

res = []
for i in range(max_num):
    if i == k:
        continue
    res.append(i)
res.append(k)
for i in range(max_num):
    j = max_num - i - 1
    if j == k:
        continue
    res.append(j)
res.append(k)
for i in range(2**(m + 1)):
    print(res[i], end=' ')
