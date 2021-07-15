#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
#= input()
N, M, X = list(map(int, input().split()))
CA = [list(map(int, input().split())) for _ in range(N)]
MAX_ANS = 10**9
ans = MAX_ANS

for i in range(2 ** N):
    buy = []
    for j in range(N):
        if (i >> j) & 1:
            buy.append(j)

    understand = [0] * (M + 1)
    money = 0
    for b in buy:
        money += CA[b][0]
        for i in range(1, M + 1):
            understand[i] += CA[b][i]

    isok = True
    for i in range(1, M + 1):
        if understand[i] < X:
            isok = False
            break

    if isok:
        ans = min(ans, money)

if ans == MAX_ANS:
    print((-1))
else:
    print(ans)

