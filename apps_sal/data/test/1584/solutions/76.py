# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 20:56:06 2020

@author: liang
"""

N = int(input())
L = [int(x) for x in input().split()]

L.sort()
ans = 0
# print(L)
for i in range(N - 2):
    # print("1:",i)
    p = i + 2
    # 以下O(2?N)　定数倍が遅い
    for j in range(i + 1, N - 1):
        # print("2",i,j)
        while p < N and L[p] < L[i] + L[j]:
            p += 1
            # print("up")
        # print(p)
        #ans += len(L[j+1:p])
        ans += max(0, p - j - 1)
print(ans)
