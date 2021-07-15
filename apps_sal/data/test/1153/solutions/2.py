# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 10:15:39 2018

@author: Nikita
"""

N, M = list(map(int, input().split()))
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
s1 = X[0]
i = 1
s2 = Y[0]
j = 1
count = 0
while i < N and j < M:
  if s1 < s2:
    s1 += X[i]
    i += 1
  elif s1 == s2:
    count += 1
    s1 += X[i]
    s2 += Y[j]
    i += 1
    j += 1
  else: # s1 > s2
    s2 += Y[j]
    j += 1
print(count + 1)

