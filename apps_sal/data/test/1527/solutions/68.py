#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**7)
import bisect
import heapq
import itertools
import math
from collections import Counter, defaultdict, deque
from copy import deepcopy
from decimal import Decimal
from math import gcd
from operator import add, itemgetter, mul, xor
def cmb(n,r,mod):
  bunshi=1
  bunbo=1
  for i in range(r):
    bunbo = bunbo*(i+1)%mod
    bunshi = bunshi*(n-i)%mod
  return (bunshi*pow(bunbo,mod-2,mod))%mod
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

#bisect.bisect_left(list,key)はlistのなかでkey未満の数字がいくつあるかを返す
#つまりlist[i] < x となる i の個数
#bisect.bisect_right(list, key)はlistのなかでkey以下の数字がいくつあるかを返す
#つまりlist[i] <= x となる i の個数
#これを応用することで
#len(list) - bisect.bisect_left(list,key)はlistのなかでkey以上の数字がいくつあるかを返す
#len(list) - bisect.bisect_right(list,key)はlistのなかでkeyより大きい数字がいくつあるかを返す
#これらを使うときはあらかじめlistをソートしておくこと！
def maze_solve(S_1,S_2,maze_list):
    d = deque()
    d.append([S_1,S_2])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while d:
        v = d.popleft()
        x = v[0]
        y = v[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                d.append([nx,ny])
    return max(list(map(lambda x: max(x), dist)))
h,w = MI()
if h==1 and w == 2:
  print(1)
elif h == 2 and w == 1:
  print(1)
else:
  ans = 0
  maze = [list(input()) for _ in range(h)]
  dist = [[-1]*w for _ in range(h)]
  start_list = []
  for i in range(h):
      for j in range(w):
          if maze[i][j] == "#":
              dist[i][j] = 0
          else:
              start_list.append([i,j])
  dist_copy = deepcopy(dist)
  for k in start_list:
      dist = deepcopy(dist_copy)
      ans = max(ans,maze_solve(k[0],k[1],maze))
  print(ans+1)
