# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 18:05:47 2020

@author: liang
"""

N, K = map(int, input().split())
A = [int(x) for x in input().split()]
visited = [-1]*N
loop = list()

cur = 1
cnt = 0
while visited[cur-1] == -1:
#while True:
    visited[cur-1] = cnt
    loop.append(cur)
    cnt += 1
    cur = A[cur-1]
    if cnt == K:
        print(cur)
        #print(loop)
        break
else:
    #print(loop)
    loop = loop[visited[cur-1]:]
    T = cnt -visited[cur-1]
    #print(loop, T)
    ans = loop[(K - cnt)%T]
    print(ans)
