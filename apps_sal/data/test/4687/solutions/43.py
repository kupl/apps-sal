"""
Created on Mon Sep 28 01:21:16 2020

@author: liang
"""
(N, K) = map(int, input().split())
num = [0] * (10 ** 5 + 1)
for i in range(N):
    (a, b) = map(int, input().split())
    num[a] += b
tmp = 0
for i in range(10 ** 5 + 1):
    tmp += num[i]
    if tmp >= K:
        print(i)
        break
