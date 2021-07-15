# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 18:25:14 2020

@author: liang
"""

H, W = map(int, input().split())

field = [input() for i in range(H)]

def Init():
    return [[-1]*W for _ in range(H)]

ans = -1

from collections import deque
q = deque()
adj = ((1,0), (-1,0), (0,1), (0,-1))
def BFS(y,x):
    def isValid(t):
        if t[0] < 0 or t[0] >= H or t[1] < 0 or t[1] >= W or field[t[0]][t[1]] == "#":
            return False
        return True
    d = Init()
    if field[y][x] == '#':
        return -1
    d[y][x] = 0
    q.append((y,x))
    res = 0
    while q:
        cur = q.popleft()
        for a in adj:
            nex = (cur[0]+a[0], cur[1]+a[1])
            if isValid(nex) and (d[nex[0]][nex[1]]== -1 or d[nex[0]][nex[1]] > d[cur[0]][cur[1]]+1):
                d[nex[0]][nex[1]] = d[cur[0]][cur[1]]+1
                #if res < d[nex[0]][nex[1]]:
                #    res = d[nex[0]][nex[1]]
                res = max(res, d[nex[0]][nex[1]])
                q.append(nex)
    return res

for i in range(H):
    for j in range(W):
        tmp = BFS(i,j)
        if tmp > ans:
            ans = tmp
print(ans)
