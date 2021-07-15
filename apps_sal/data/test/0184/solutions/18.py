# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 09:54:56 2018

@author: Nikita
"""

L, R, A = list(map(int, input().split()))
if L <= R:
  if A < R - L:
    print(2 * (L + A))
  else:
    A -= (R - L)
    print(2 * (R + A // 2))
else:
  if A < L - R:
    print(2 * (R + A))
  else:
    A -= (L - R)
    print(2 * (L + A // 2))

