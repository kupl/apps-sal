# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 20:18:57 2020

@author: liang
"""

N = int(input())
S = input()

tmp = 0

for i in range(1, N):
    if S[i] == "E":
        tmp += 1

ans = 10**6
for i in range(N):
    if ans > tmp:
        ans = tmp
    if i == N - 1:
        break
    if S[i] == "W":
        tmp += 1
    if S[i + 1] == "E":
        tmp -= 1
    # print(tmp)

print(ans)
