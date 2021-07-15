import sys
import itertools
# import numpy as np
import time
import math
from heapq import heappop, heappush
from collections import defaultdict
from collections import Counter
from collections import deque
from itertools import permutations
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())
import queue

N, M = list(map(int, input().split()))
if M == 0:
    print((-1))
    return
adj = [[] for _ in range(N)]
for i in range(M):
    u, v = list(map(int, input().split()))    
    u -= 1
    v -= 1
    adj[u].append(v)
S, T = list(map(int, input().split()))
S -= 1
T -= 1

dist = [[INF,INF,INF] for _ in range(N+1)]
 
d = 0
q = [S]
while q:
  d += 1
  r = d % 3
  qq = []
  for u in q:
    for v in adj[u]:
      if dist[v][r] == INF:
        dist[v][r] = d
        qq.append(v)
  q = qq
 
d = dist[T][0]
answer = -1 if d == INF else d // 3
print(answer)



