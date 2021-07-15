# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 16:58:10 2020

@author: liang
"""


"""
【パディングはソート後】
"""
N = int(input())
A = [int(input()) for _ in range(N)]
A.sort()
A += [-1]
ans = 0
count = 1
for i in range(N):
    #print(count)
    if A[i] == A[i+1]:
        #print("A")
        count += 1
    else:
        #print("B")
        if count%2 == 1:
            ans += 1
        count = 1
print(ans)
