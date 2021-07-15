#!/usr/bin/env python3
import sys
sys.setrecursionlimit(1000000)
from collections import deque

# スペース区切りの整数の入力
H, W = list(map(int, input().split()))

#配列の入力
s = [list(input()) for _ in range(H)]

dist = [[-1 for _ in range(W)]for _ in range(H)]


def bfs():
    que = deque()
    que.append((0, 0))
    dist[0][0] = 0
    offset = ((1,0),(-1,0),(0,1),(0,-1))
    while que:
        now_h, now_w = que.popleft()
        if now_h < 0 or H-1 < now_h or now_w < 0 or W-1 < now_w:
            continue
        if s[now_h][now_w] == '#':
            continue
        for oh, ow in offset:
            if now_h+oh < 0 or H-1 < now_h+oh or now_w+ow < 0 or W-1 < now_w+ow:
                continue
            if dist[now_h+oh][now_w+ow] != -1:
                continue
            else:
                dist[now_h+oh][now_w+ow] = dist[now_h][now_w]+1
                que.append((now_h+oh, now_w+ow))





bfs()
m = dist[H-1][W-1]

if m == -1:
    print((-1))
else:
    count = 0
    for t in s:
        count += t.count('.')
    
    print((count - m- 1))


