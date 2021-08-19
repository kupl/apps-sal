# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 11:05:00 2020

@author: liang
"""

"""
片側を固定して、それぞれのケースに対して最適解を求める
それぞれのケースについて
index(b_i) =< index(b_i-1)
であるから、bの最大値bestを保存して探索することで重複探索を回避できる
"""
N, M, K = map(int, input().split())

A = [0] + [int(x) for x in input().split()]
B = [0] + [int(x) for x in input().split()]

s_b = 0
for i in range(M + 1):
    s_b += B[i]
    if s_b > K:
        s_b -= B[i]
        best = i - 1
        break
else:
    best = M
res = best
# print(res)
s_a = 0
for i in range(N + 1):
   # print("i", i)
    s_a += A[i]
    if s_a > K:
        break
    for j in reversed(range(best + 1)):
        # print("j",j)
        if s_b <= K - s_a:
            if i + j > res:
                res = i + j
            best = j
            #print(i, j, s_a, s_b)
            break
        else:
            s_b -= B[j]

print(res)
