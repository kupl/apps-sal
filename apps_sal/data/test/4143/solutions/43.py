# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 23:38:36 2020

@author: liang
"""

N = int(input())
cost = [int(input()) for _ in range(5)]
cost.sort()
if N%cost[0] == 0:
    ans = 4 + N//cost[0] 
else:
    ans = 4 + N//cost[0] + 1
print(ans)
