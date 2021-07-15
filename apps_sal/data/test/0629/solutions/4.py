#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N = int(input())

A1s = list(map(int,input().split()))
A2s = list(map(int,input().split()))
Bs = list(map(int,input().split()))

scores = []
score = 0
for n in range(N):
    if n == 0:
        score = Bs[0] + sum(A2s)
    else:
        score -= Bs[n-1]
        score += Bs[n]
        score -= A2s[n-1]
        score += A1s[n-1]
    scores.append(score)
scores.sort()
print(sum(scores[:2]))


